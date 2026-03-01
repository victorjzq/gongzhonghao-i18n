#!/usr/bin/env python3
"""
Medium 批量发布脚本
用法: python publish_medium.py --lang en --status draft
"""

import os
import json
import time
import argparse
import requests
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent
TRANSLATED_DIR = BASE_DIR / "translated"
LOGS_DIR = BASE_DIR / "logs"
PUBLISH_LOG = LOGS_DIR / "publish_log.json"

MEDIUM_API_BASE = "https://api.medium.com/v1"

LANG_TAGS = {
    "en": ["price-action", "trading", "al-brooks", "technical-analysis"],
    "vi": ["price-action", "giao-dich", "phan-tich-ky-thuat"],
    "id": ["price-action", "trading", "analisis-teknikal"],
    "es": ["price-action", "trading", "analisis-tecnico"],
    "pt": ["price-action", "trading", "analise-tecnica"],
    "ja": ["price-action", "trading", "テクニカル分析"],
    "ko": ["price-action", "trading", "기술적분석"],
    "de": ["price-action", "trading", "technische-analyse"],
    "ar": ["price-action", "trading"],
    "ru": ["price-action", "trading", "технический-анализ"],
}


def get_medium_token():
    token = os.environ.get("MEDIUM_TOKEN")
    if not token:
        env_file = BASE_DIR / ".env"
        if env_file.exists():
            for line in env_file.read_text().splitlines():
                if line.startswith("MEDIUM_TOKEN="):
                    token = line.split("=", 1)[1].strip().strip('"').strip("'")
    if not token:
        raise ValueError("MEDIUM_TOKEN not found. Set it in .env or environment.")
    return token


def get_user_id(token):
    resp = requests.get(
        f"{MEDIUM_API_BASE}/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    resp.raise_for_status()
    return resp.json()["data"]["id"]


def publish_article(token, user_id, title, content, tags, status="draft"):
    resp = requests.post(
        f"{MEDIUM_API_BASE}/users/{user_id}/posts",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        json={
            "title": title,
            "contentFormat": "markdown",
            "content": content,
            "tags": tags[:5],  # Medium allows max 5 tags
            "publishStatus": status,
        },
    )
    resp.raise_for_status()
    return resp.json()["data"]


def load_publish_log():
    if PUBLISH_LOG.exists():
        return json.loads(PUBLISH_LOG.read_text())
    return {"publications": [], "stats": {"total_published": 0}}


def save_publish_log(log):
    PUBLISH_LOG.write_text(json.dumps(log, ensure_ascii=False, indent=2))


def extract_title(content):
    for line in content.splitlines():
        line = line.strip()
        if line and not line.startswith("![") and not line.startswith("---"):
            # Remove markdown heading markers
            return line.lstrip("#").strip().rstrip("=").strip()
    return "Untitled"


def main():
    parser = argparse.ArgumentParser(description="Publish articles to Medium")
    parser.add_argument("--lang", required=True, help="Language code (en, vi, etc.)")
    parser.add_argument("--status", default="draft", choices=["draft", "public"])
    parser.add_argument("--category", help="Only publish specific category")
    parser.add_argument("--limit", type=int, default=0, help="Max articles to publish")
    parser.add_argument("--delay", type=int, default=30, help="Delay between posts (seconds)")
    args = parser.parse_args()

    token = get_medium_token()
    user_id = get_user_id(token)
    print(f"Authenticated as user: {user_id}")

    lang_dir = TRANSLATED_DIR / args.lang
    if not lang_dir.exists():
        print(f"No translated files for language: {args.lang}")
        return

    log = load_publish_log()
    published_keys = {p["source_file"] for p in log["publications"]}

    md_files = sorted(lang_dir.rglob("*.md"))
    if args.category:
        md_files = [f for f in md_files if args.category in str(f)]

    count = 0
    for md_file in md_files:
        rel_path = str(md_file.relative_to(TRANSLATED_DIR))
        if rel_path in published_keys:
            print(f"  SKIP (already published): {rel_path}")
            continue

        content = md_file.read_text()
        title = extract_title(content)
        tags = LANG_TAGS.get(args.lang, ["price-action", "trading"])

        try:
            result = publish_article(token, user_id, title, content, tags, args.status)
            print(f"  OK: {title} -> {result['url']}")

            log["publications"].append({
                "source_file": rel_path,
                "platform": "medium",
                "language": args.lang,
                "title": title,
                "url": result["url"],
                "medium_id": result["id"],
                "status": args.status,
                "published_at": datetime.now().isoformat(),
            })
            log["stats"]["total_published"] += 1
            log["stats"]["medium_published"] = log["stats"].get("medium_published", 0) + 1
            save_publish_log(log)

            count += 1
            if args.limit and count >= args.limit:
                print(f"Reached limit of {args.limit} articles.")
                break

            time.sleep(args.delay)

        except Exception as e:
            print(f"  FAIL: {title} -> {e}")
            log.setdefault("failed_publications", []).append({
                "source_file": rel_path,
                "platform": "medium",
                "error": str(e),
                "timestamp": datetime.now().isoformat(),
            })
            save_publish_log(log)

    print(f"\nDone. Published {count} articles to Medium ({args.status}).")


if __name__ == "__main__":
    main()
