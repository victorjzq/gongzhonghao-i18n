#!/usr/bin/env python3
"""Dev.to 流量统计 — 查询真实浏览量、反应数、评论数。

用法:
    python devto_stats.py               # 完整报告
    python devto_stats.py --top 10      # Top 10 文章
    python devto_stats.py --json        # JSON 输出
"""

import argparse
import json
import os
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    print("❌ requests 未安装: pip install requests")
    sys.exit(1)


DEVTO_API = "https://dev.to/api"


def get_api_key() -> str:
    """从多路径查找 Dev.to API key。"""
    # 1. 环境变量
    key = os.environ.get("DEVTO_API_KEY") or os.environ.get("DEV_TO_API_KEY")
    if key:
        return key

    # 2. 多个配置文件
    search_paths = [
        "~/Claude-Global/公众号国际化/.env",
        "~/.openclaw/wecom.env",
    ]
    for path in search_paths:
        expanded = os.path.expanduser(path)
        if os.path.exists(expanded):
            try:
                with open(expanded) as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith("#") or "=" not in line:
                            continue
                        line = line.replace("export ", "", 1)
                        k, v = line.split("=", 1)
                        k = k.strip()
                        if k in ("DEVTO_API_KEY", "DEV_TO_API_KEY"):
                            return v.strip().strip('"').strip("'")
            except Exception:
                continue

    return ""


def fetch_all_articles(api_key: str) -> list:
    """分页获取所有已发布文章。"""
    headers = {"api-key": api_key}
    all_articles = []
    page = 1

    while True:
        try:
            r = requests.get(
                f"{DEVTO_API}/articles/me",
                headers=headers,
                params={"per_page": 1000, "page": page},
                timeout=30,
            )
            if r.status_code == 401:
                return []  # invalid key
            r.raise_for_status()
            articles = r.json()
            if not articles:
                break
            all_articles.extend(articles)
            if len(articles) < 1000:
                break
            page += 1
        except requests.RequestException as e:
            print(f"⚠️ API 请求失败 (page {page}): {e}", file=sys.stderr)
            break

    return all_articles


def get_stats(top_n: int = 5) -> str:
    """获取完整流量统计。"""
    api_key = get_api_key()
    if not api_key:
        return (
            "❌ 没有 Dev.to API key\n"
            "请去 https://dev.to/settings/extensions 获取 API key\n"
            "然后在企业微信发：\n"
            "执行 echo 'DEVTO_API_KEY=你的key' >> ~/.openclaw/wecom.env"
        )

    articles = fetch_all_articles(api_key)
    if not articles:
        return "❌ 获取文章失败，请检查 API key 是否有效"

    # 统计
    total_views = sum(a.get("page_views_count", 0) for a in articles)
    total_reactions = sum(a.get("positive_reactions_count", 0) for a in articles)
    total_comments = sum(a.get("comments_count", 0) for a in articles)
    n = len(articles)
    avg_views = total_views // max(n, 1)

    # 按浏览量排序
    top = sorted(
        articles,
        key=lambda x: x.get("page_views_count", 0),
        reverse=True,
    )[:top_n]

    # 最新发布
    recent = sorted(
        articles,
        key=lambda x: x.get("published_at", ""),
        reverse=True,
    )[:3]

    lines = [f"📊 Dev.to 流量报告（共 {n} 篇）\n"]
    lines.append(f"👀 总浏览量: {total_views:,}")
    lines.append(f"❤️ 总反应数: {total_reactions:,}")
    lines.append(f"💬 总评论数: {total_comments:,}")
    lines.append(f"📈 篇均浏览: {avg_views:,}")

    lines.append(f"\n🏆 浏览量 Top {top_n}:")
    for a in top:
        views = a.get("page_views_count", 0)
        reactions = a.get("positive_reactions_count", 0)
        title = a.get("title", "")[:40]
        lines.append(f"  {views:>6,} 👀 {reactions:>3} ❤️ | {title}")

    lines.append(f"\n📅 最新发布:")
    for a in recent:
        date = a.get("published_at", "")[:10]
        views = a.get("page_views_count", 0)
        title = a.get("title", "")[:35]
        lines.append(f"  {date} | {views:>5,} 👀 | {title}")

    return "\n".join(lines)


def get_stats_json() -> dict:
    """JSON 格式输出。"""
    api_key = get_api_key()
    if not api_key:
        return {"error": "no API key"}

    articles = fetch_all_articles(api_key)
    if not articles:
        return {"error": "fetch failed"}

    return {
        "total_articles": len(articles),
        "total_views": sum(a.get("page_views_count", 0) for a in articles),
        "total_reactions": sum(a.get("positive_reactions_count", 0) for a in articles),
        "total_comments": sum(a.get("comments_count", 0) for a in articles),
        "top_5": [
            {
                "title": a.get("title", ""),
                "views": a.get("page_views_count", 0),
                "reactions": a.get("positive_reactions_count", 0),
                "url": a.get("url", ""),
            }
            for a in sorted(
                articles,
                key=lambda x: x.get("page_views_count", 0),
                reverse=True,
            )[:5]
        ],
    }


def main():
    parser = argparse.ArgumentParser(description="Dev.to 流量统计")
    parser.add_argument("--top", type=int, default=5, help="Top N 文章")
    parser.add_argument("--json", action="store_true", help="JSON 输出")
    args = parser.parse_args()

    if args.json:
        print(json.dumps(get_stats_json(), ensure_ascii=False, indent=2))
    else:
        print(get_stats(top_n=args.top))


if __name__ == "__main__":
    main()
