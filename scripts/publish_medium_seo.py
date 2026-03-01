#!/usr/bin/env python3
"""
Medium SEO 精品发布脚本 — 从 medium_batch1.json 读取精选文章，
用 SEO 优化标题发布到 Medium。

用法:
  python scripts/publish_medium_seo.py --dry-run         # 预览
  python scripts/publish_medium_seo.py --limit 5          # 发 5 篇
  python scripts/publish_medium_seo.py --status public    # 直接公开
  python scripts/publish_medium_seo.py                    # 全部发（draft）
"""

import os
import json
import time
import argparse
import requests
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent
TRANSLATED_EN_DIR = BASE_DIR / "translated" / "en"
LOGS_DIR = BASE_DIR / "logs"
PUBLISH_LOG = LOGS_DIR / "publish_log.json"
BATCH_FILE = LOGS_DIR / "medium_batch1.json"

MEDIUM_API_BASE = "https://api.medium.com/v1"
MEDIUM_TAGS = ["price-action", "trading", "al-brooks", "day-trading", "technical-analysis"]

# 每篇间隔（秒）— 模拟人工发布节奏
PUBLISH_DELAY = 60


def get_medium_token():
    token = os.environ.get("MEDIUM_TOKEN")
    if not token:
        env_file = BASE_DIR / ".env"
        if env_file.exists():
            for line in env_file.read_text().splitlines():
                if line.startswith("MEDIUM_TOKEN="):
                    token = line.split("=", 1)[1].strip().strip('"').strip("'")
    if not token:
        raise ValueError(
            "MEDIUM_TOKEN not found.\n"
            "获取方法: https://medium.com/me/settings/security → Integration tokens\n"
            "设置方法: echo 'MEDIUM_TOKEN=xxx' >> ~/Claude-Global/公众号国际化/.env"
        )
    return token


def get_user_id(token):
    resp = requests.get(
        f"{MEDIUM_API_BASE}/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    resp.raise_for_status()
    data = resp.json()["data"]
    print(f"✅ Medium 用户: {data['username']} (id: {data['id']})")
    return data["id"]


def add_seo_footer(content, title):
    """在文章末尾添加 SEO 友好的 footer"""
    footer = (
        "\n\n---\n\n"
        "*This article is part of the **Al Brooks Price Action Trading Notes** series. "
        "Follow for more price action analysis, trading psychology insights, and book reviews.*\n\n"
        "*Tags: #PriceAction #AlBrooks #DayTrading #TradingPsychology #TechnicalAnalysis*\n"
    )
    return content + footer


def publish_article(token, user_id, title, content, tags, status="draft"):
    """发布单篇文章到 Medium"""
    content_with_footer = add_seo_footer(content, title)

    resp = requests.post(
        f"{MEDIUM_API_BASE}/users/{user_id}/posts",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        json={
            "title": title,
            "contentFormat": "markdown",
            "content": content_with_footer,
            "tags": tags[:5],
            "publishStatus": status,
        },
    )
    resp.raise_for_status()
    return resp.json()["data"]


def load_publish_log():
    if PUBLISH_LOG.exists():
        return json.loads(PUBLISH_LOG.read_text())
    return {"metadata": {}, "publications": []}


def save_publish_log(log):
    PUBLISH_LOG.write_text(json.dumps(log, ensure_ascii=False, indent=2))


def main():
    parser = argparse.ArgumentParser(description="Medium SEO 精品发布")
    parser.add_argument("--status", default="draft", choices=["draft", "public"])
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--delay", type=int, default=PUBLISH_DELAY)
    args = parser.parse_args()

    # 读取精选列表
    if not BATCH_FILE.exists():
        print("❌ 找不到 logs/medium_batch1.json，请先运行选文脚本")
        return

    with open(BATCH_FILE) as f:
        batch = json.load(f)

    print(f"📋 精选文章: {len(batch)} 篇")

    if not args.dry_run:
        token = get_medium_token()
        user_id = get_user_id(token)

    log = load_publish_log()
    published_sources = {
        p["source"]
        for p in log.get("publications", [])
        if p.get("platform") == "medium"
    }

    count = 0
    skipped = 0

    for i, article in enumerate(batch, 1):
        source = article["path"]
        seo_title = article.get("seo_title", article["title"])

        # 检查是否已发布
        if source in published_sources:
            print(f"  SKIP [{i}/{len(batch)}] (已发布): {seo_title[:60]}")
            skipped += 1
            continue

        # 读取文章内容
        full_path = TRANSLATED_EN_DIR / source
        if not full_path.exists():
            print(f"  MISS [{i}/{len(batch)}] 文件不存在: {source}")
            continue

        content = full_path.read_text()

        if args.dry_run:
            print(f"  DRY  [{i}/{len(batch)}] {seo_title}")
            count += 1
        else:
            try:
                result = publish_article(
                    token, user_id, seo_title, content, MEDIUM_TAGS, args.status
                )
                url = result.get("url", "no-url")
                print(f"  ✅   [{i}/{len(batch)}] {seo_title[:50]}...")
                print(f"       → {url}")

                log["publications"].append({
                    "date": datetime.now().strftime("%Y-%m-%d"),
                    "platform": "medium",
                    "language": "en",
                    "source": source,
                    "title": seo_title,
                    "url": url,
                    "medium_id": result.get("id"),
                    "status": args.status,
                })
                save_publish_log(log)

                count += 1
                if args.limit and count >= args.limit:
                    print(f"\n⏸️  达到限制: {args.limit} 篇")
                    break

                if i < len(batch):
                    print(f"       ⏳ 等待 {args.delay}s...")
                    time.sleep(args.delay)

            except Exception as e:
                print(f"  ❌   [{i}/{len(batch)}] {seo_title[:50]} → {e}")

    print(f"\n{'📝 预览' if args.dry_run else '✅ 完成'}: {count} 篇 | 跳过: {skipped}")


if __name__ == "__main__":
    main()
