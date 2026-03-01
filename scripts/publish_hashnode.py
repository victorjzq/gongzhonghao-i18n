#!/usr/bin/env python3
"""
Hashnode SEO 精品发布脚本 — 用 GraphQL API 发布到 Hashnode。

用法:
  python scripts/publish_hashnode.py --dry-run              # 预览
  python scripts/publish_hashnode.py --limit 5              # 发 5 篇
  python scripts/publish_hashnode.py                        # 全部发
  python scripts/publish_hashnode.py --setup                # 获取 publication ID

配置（写入 .env）:
  HASHNODE_TOKEN=xxx        # https://hashnode.com/settings/developer
  HASHNODE_PUB_ID=xxx       # 用 --setup 获取
"""

import os
import json
import time
import argparse
import requests
import re
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent
TRANSLATED_EN_DIR = BASE_DIR / "translated" / "en"
LOGS_DIR = BASE_DIR / "logs"
PUBLISH_LOG = LOGS_DIR / "publish_log.json"
BATCH_FILE = LOGS_DIR / "medium_batch1.json"

HASHNODE_GQL = "https://gql.hashnode.com"
HASHNODE_TAGS = [
    {"name": "Price Action", "slug": "price-action"},
    {"name": "Trading", "slug": "trading"},
    {"name": "Day Trading", "slug": "day-trading"},
    {"name": "Technical Analysis", "slug": "technical-analysis"},
]

PUBLISH_DELAY = 10  # Hashnode 允许 500 mutations/min，10s 很安全


def load_env():
    """从 .env 加载配置"""
    env = {}
    env_file = BASE_DIR / ".env"
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            if "=" in line and not line.startswith("#"):
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def get_token():
    token = os.environ.get("HASHNODE_TOKEN")
    if not token:
        token = load_env().get("HASHNODE_TOKEN")
    if not token:
        raise ValueError(
            "HASHNODE_TOKEN not found.\n"
            "获取: https://hashnode.com/settings/developer\n"
            "设置: echo 'HASHNODE_TOKEN=xxx' >> .env"
        )
    return token


def get_pub_id():
    pub_id = os.environ.get("HASHNODE_PUB_ID")
    if not pub_id:
        pub_id = load_env().get("HASHNODE_PUB_ID")
    if not pub_id:
        raise ValueError(
            "HASHNODE_PUB_ID not found.\n"
            "先运行: python scripts/publish_hashnode.py --setup"
        )
    return pub_id


def gql(token, query, variables=None):
    """执行 GraphQL 请求"""
    resp = requests.post(
        HASHNODE_GQL,
        headers={
            "Authorization": token,
            "Content-Type": "application/json",
        },
        json={"query": query, "variables": variables or {}},
    )
    resp.raise_for_status()
    data = resp.json()
    if "errors" in data:
        raise Exception(f"GraphQL errors: {data['errors']}")
    return data["data"]


def setup(token):
    """获取用户信息和 publication ID"""
    data = gql(token, """
    {
      me {
        id
        username
        publications(first: 5) {
          edges {
            node {
              id
              title
              url
            }
          }
        }
      }
    }
    """)
    me = data["me"]
    print(f"✅ 用户: {me['username']} (id: {me['id']})")
    pubs = me["publications"]["edges"]
    if pubs:
        for p in pubs:
            node = p["node"]
            print(f"   Publication: {node['title']}")
            print(f"   ID: {node['id']}")
            print(f"   URL: {node['url']}")
        pub_id = pubs[0]["node"]["id"]
        print(f"\n👉 将以下行添加到 .env:")
        print(f"   HASHNODE_PUB_ID={pub_id}")
    else:
        print("❌ 没有找到 publication，请先在 hashnode.com 创建一个博客")


def title_to_slug(title):
    """生成 URL-friendly slug"""
    slug = title.lower()
    slug = re.sub(r'["\':,—?!()]+', '', slug)
    slug = re.sub(r'[^a-z0-9]+', '-', slug)
    slug = slug.strip('-')[:80]
    return slug


def add_seo_footer(content):
    """添加 SEO 友好的 footer"""
    return content + (
        "\n\n---\n\n"
        "*This article is part of the **Al Brooks Price Action Trading Notes** series. "
        "Follow for more price action analysis, trading psychology insights, and book reviews.*\n"
    )


def publish_post(token, pub_id, title, content, tags, slug=None):
    """发布文章到 Hashnode"""
    data = gql(
        token,
        """
        mutation PublishPost($input: PublishPostInput!) {
          publishPost(input: $input) {
            post {
              id
              title
              slug
              url
            }
          }
        }
        """,
        {
            "input": {
                "publicationId": pub_id,
                "title": title,
                "contentMarkdown": add_seo_footer(content),
                "tags": tags,
                "slug": slug or title_to_slug(title),
            }
        },
    )
    return data["publishPost"]["post"]


def load_publish_log():
    if PUBLISH_LOG.exists():
        return json.loads(PUBLISH_LOG.read_text())
    return {"metadata": {}, "publications": []}


def save_publish_log(log):
    PUBLISH_LOG.write_text(json.dumps(log, ensure_ascii=False, indent=2))


def main():
    parser = argparse.ArgumentParser(description="Hashnode SEO 精品发布")
    parser.add_argument("--setup", action="store_true", help="获取 publication ID")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--delay", type=int, default=PUBLISH_DELAY)
    parser.add_argument("--all-en", action="store_true", help="发布所有英文文章（不仅精选）")
    args = parser.parse_args()

    token = get_token()

    if args.setup:
        setup(token)
        return

    pub_id = get_pub_id()

    # 确定发布列表
    if args.all_en:
        # 扫描所有英文翻译
        articles = []
        for md in sorted(TRANSLATED_EN_DIR.rglob("*.md")):
            with open(md) as f:
                first_line = f.readline().strip().lstrip("#").strip()
            articles.append({
                "path": str(md.relative_to(TRANSLATED_EN_DIR)),
                "title": first_line,
                "seo_title": first_line,
                "full_path": str(md),
            })
        print(f"📋 全部英文文章: {len(articles)} 篇")
    else:
        if not BATCH_FILE.exists():
            print("❌ 找不到 logs/medium_batch1.json")
            return
        with open(BATCH_FILE) as f:
            articles = json.load(f)
        print(f"📋 精选文章: {len(articles)} 篇")

    log = load_publish_log()
    published = {
        p["source"]
        for p in log.get("publications", [])
        if p.get("platform") == "hashnode"
    }

    count = 0
    skipped = 0

    for i, article in enumerate(articles, 1):
        source = article["path"]
        title = article.get("seo_title", article["title"])

        if source in published:
            skipped += 1
            continue

        full_path = TRANSLATED_EN_DIR / source
        if not full_path.exists():
            print(f"  MISS [{i}] {source}")
            continue

        content = full_path.read_text()

        if args.dry_run:
            print(f"  DRY  [{i}] {title[:70]}")
            count += 1
        else:
            try:
                post = publish_post(token, pub_id, title, content, HASHNODE_TAGS)
                print(f"  ✅   [{i}] {title[:50]}...")
                print(f"       → {post['url']}")

                log["publications"].append({
                    "date": datetime.now().strftime("%Y-%m-%d"),
                    "platform": "hashnode",
                    "language": "en",
                    "source": source,
                    "title": title,
                    "url": post["url"],
                    "hashnode_id": post["id"],
                    "status": "published",
                })
                save_publish_log(log)

                count += 1
                if args.limit and count >= args.limit:
                    print(f"\n⏸️  达到限制: {args.limit} 篇")
                    break

                if count < len(articles):
                    time.sleep(args.delay)

            except Exception as e:
                print(f"  ❌   [{i}] {title[:50]} → {e}")

    print(f"\n{'📝 预览' if args.dry_run else '✅ 完成'}: {count} 篇发布 | {skipped} 跳过")


if __name__ == "__main__":
    main()
