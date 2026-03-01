#!/usr/bin/env python3
"""
Dev.to 批量发布脚本
用法: python publish_devto.py --lang en --status draft
Dev.to API: https://developers.forem.com/api/v1
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

DEVTO_API_BASE = "https://dev.to/api"

LANG_TAGS = {
    "en": ["priceaction", "trading", "albrooks", "technicalanalysis", "finance"],
    "vi": ["priceaction", "trading", "vietnam", "technicalanalysis"],
    "id": ["priceaction", "trading", "indonesia", "technicalanalysis"],
    "es": ["priceaction", "trading", "spanish", "technicalanalysis"],
    "pt": ["priceaction", "trading", "portuguese", "technicalanalysis"],
    "ja": ["priceaction", "trading", "japanese", "technicalanalysis"],
    "ko": ["priceaction", "trading", "korean", "technicalanalysis"],
    "de": ["priceaction", "trading", "german", "technicalanalysis"],
    "ar": ["priceaction", "trading", "arabic", "technicalanalysis"],
    "ru": ["priceaction", "trading", "russian", "technicalanalysis"],
}


def get_devto_key():
    key = os.environ.get("DEVTO_API_KEY")
    if not key:
        env_file = BASE_DIR / ".env"
        if env_file.exists():
            for line in env_file.read_text().splitlines():
                if line.startswith("DEVTO_API_KEY="):
                    key = line.split("=", 1)[1].strip().strip('"').strip("'")
    if not key:
        raise ValueError("DEVTO_API_KEY not found. Set it in .env or environment.")
    return key


def publish_article(api_key, title, content, tags, published=False):
    resp = requests.post(
        f"{DEVTO_API_BASE}/articles",
        headers={
            "api-key": api_key,
            "Content-Type": "application/json",
        },
        json={
            "article": {
                "title": title,
                "body_markdown": content,
                "tags": tags[:4],  # Dev.to allows max 4 tags
                "published": published,
            }
        },
    )
    if resp.status_code == 429:
        raise RateLimitError("429 Too Many Requests")
    resp.raise_for_status()
    return resp.json()


class RateLimitError(Exception):
    pass


def extract_title(content):
    lines = content.splitlines()
    # Priority 1: Find # heading
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#") and not stripped.startswith("#!"):
            return stripped.lstrip("#").strip()
    # Priority 2: Find setext heading (line followed by === or ---)
    for i, line in enumerate(lines):
        stripped = line.strip()
        if i + 1 < len(lines):
            next_line = lines[i + 1].strip()
            if next_line and all(c == "=" for c in next_line) and stripped:
                return stripped
    # Fallback: first non-empty, non-image line (truncated to 80 chars)
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith("![") and not stripped.startswith("---"):
            title = stripped.lstrip("#").strip().rstrip("=").strip()
            # Remove markdown bold
            title = title.replace("**", "")
            return title[:80] if len(title) > 80 else title
    return "Untitled"


def load_publish_log():
    if PUBLISH_LOG.exists():
        return json.loads(PUBLISH_LOG.read_text())
    return {"publications": [], "stats": {"total_published": 0}}


def save_publish_log(log):
    PUBLISH_LOG.write_text(json.dumps(log, ensure_ascii=False, indent=2))


def main():
    parser = argparse.ArgumentParser(description="Publish articles to Dev.to")
    parser.add_argument("--lang", required=True, help="Language code (en, vi, etc.)")
    parser.add_argument(
        "--status",
        default="draft",
        choices=["draft", "public"],
        help="draft or public",
    )
    parser.add_argument("--category", help="Only publish specific category")
    parser.add_argument("--limit", type=int, default=0, help="Max articles to publish")
    parser.add_argument(
        "--delay", type=int, default=120, help="Delay between posts (seconds)"
    )
    args = parser.parse_args()

    api_key = get_devto_key()
    published = args.status == "public"
    print(f"Publishing to Dev.to as {'public' if published else 'draft'}")

    lang_dir = TRANSLATED_DIR / args.lang
    if not lang_dir.exists():
        print(f"No translated files for language: {args.lang}")
        return

    log = load_publish_log()
    published_keys = set()
    for p in log["publications"]:
        if p.get("platform") == "devto":
            if "source_file" in p:
                published_keys.add(p["source_file"])
            if "source" in p:
                published_keys.add(p["source"])
                # Also add the full relative path format
                published_keys.add(f"{args.lang}/{p['source']}")

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
        tags = LANG_TAGS.get(args.lang, ["priceaction", "trading"])

        success = False
        for retry in range(3):
            try:
                result = publish_article(api_key, title, content, tags, published)
                url = result.get("url", "")
                article_id = result.get("id", "unknown")
                print(f"  OK: {title} -> {url}")

                log["publications"].append({
                    "source_file": rel_path,
                    "platform": "devto",
                    "language": args.lang,
                    "title": title,
                    "url": url,
                    "devto_id": article_id,
                    "status": args.status,
                    "published_at": datetime.now().isoformat(),
                })
                log["stats"]["total_published"] += 1
                log["stats"]["devto_published"] = (
                    log["stats"].get("devto_published", 0) + 1
                )
                save_publish_log(log)
                success = True
                break

            except RateLimitError:
                wait = 60 * (retry + 1)
                print(f"  RATE LIMITED: waiting {wait}s before retry {retry+1}/3...")
                time.sleep(wait)
            except (requests.exceptions.HTTPError, Exception) as e:
                print(f"  FAIL: {title} -> {e}")
                log.setdefault("failed_publications", []).append({
                    "source_file": rel_path,
                    "platform": "devto",
                    "error": str(e),
                    "timestamp": datetime.now().isoformat(),
                })
                save_publish_log(log)
                break

        if success:
            count += 1
            if args.limit and count >= args.limit:
                print(f"Reached limit of {args.limit} articles.")
                break
            time.sleep(args.delay)
        elif retry == 2:
            print(f"  GIVING UP after 3 retries: {title}")
            break  # Stop trying more articles if rate limited 3 times

    print(f"\nDone. Published {count} articles to Dev.to ({args.status}).")


if __name__ == "__main__":
    main()
