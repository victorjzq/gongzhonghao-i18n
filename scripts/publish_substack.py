#!/usr/bin/env python3
"""
Substack 批量发布脚本（通过内部 API）
用法: python publish_substack.py --lang en --subdomain your-newsletter
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
TRANSLATED_DIR = BASE_DIR / "translated"
LOGS_DIR = BASE_DIR / "logs"
PUBLISH_LOG = LOGS_DIR / "publish_log.json"


def get_substack_cookie():
    cookie = os.environ.get("SUBSTACK_SID")
    if not cookie:
        env_file = BASE_DIR / ".env"
        if env_file.exists():
            for line in env_file.read_text().splitlines():
                if line.startswith("SUBSTACK_SID="):
                    cookie = line.split("=", 1)[1].strip().strip('"').strip("'")
    if not cookie:
        raise ValueError("SUBSTACK_SID not found. Set it in .env or environment.")
    return cookie


def markdown_to_prosemirror(md_text):
    """Convert markdown to simplified ProseMirror JSON structure."""
    content = []
    lines = md_text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]

        # Skip empty lines
        if not line.strip():
            i += 1
            continue

        # Skip image lines (WeChat images won't work on Substack)
        if line.strip().startswith("!["):
            i += 1
            continue

        # Horizontal rule
        if line.strip() in ("---", "* * *", "***"):
            content.append({"type": "horizontal_rule"})
            i += 1
            continue

        # Headings
        heading_match = re.match(r"^(#{1,6})\s+(.*)", line)
        if heading_match:
            level = len(heading_match.group(1))
            text = heading_match.group(2).strip()
            content.append({
                "type": "heading",
                "attrs": {"level": level},
                "content": [{"type": "text", "text": text}],
            })
            i += 1
            continue

        # Setext headings (underline style)
        if i + 1 < len(lines) and re.match(r"^=+\s*$", lines[i + 1]):
            content.append({
                "type": "heading",
                "attrs": {"level": 1},
                "content": [{"type": "text", "text": line.strip()}],
            })
            i += 2
            continue
        if i + 1 < len(lines) and re.match(r"^-+\s*$", lines[i + 1]):
            content.append({
                "type": "heading",
                "attrs": {"level": 2},
                "content": [{"type": "text", "text": line.strip()}],
            })
            i += 2
            continue

        # Blockquote
        if line.startswith("> "):
            text = line[2:].strip()
            content.append({
                "type": "blockquote",
                "content": [
                    {
                        "type": "paragraph",
                        "content": [{"type": "text", "text": text}],
                    }
                ],
            })
            i += 1
            continue

        # List items
        list_match = re.match(r"^[\*\-]\s+(.*)", line)
        numbered_match = re.match(r"^\d+\.\s+(.*)", line)
        if list_match or numbered_match:
            items = []
            list_type = "ordered_list" if numbered_match else "bullet_list"
            while i < len(lines):
                m = re.match(r"^[\*\-]\s+(.*)", lines[i]) or re.match(
                    r"^\d+\.\s+(.*)", lines[i]
                )
                if not m:
                    break
                items.append({
                    "type": "list_item",
                    "content": [
                        {
                            "type": "paragraph",
                            "content": [{"type": "text", "text": m.group(1).strip()}],
                        }
                    ],
                })
                i += 1
            content.append({"type": list_type, "content": items})
            continue

        # Regular paragraph
        # Collect multi-line paragraph
        para_lines = [line]
        i += 1
        while i < len(lines) and lines[i].strip() and not lines[i].startswith("#"):
            if lines[i].strip() in ("---", "* * *", "***"):
                break
            if lines[i].startswith("> "):
                break
            if re.match(r"^[\*\-]\s+", lines[i]):
                break
            if re.match(r"^\d+\.\s+", lines[i]):
                break
            if lines[i].strip().startswith("!["):
                break
            para_lines.append(lines[i])
            i += 1

        text = " ".join(l.strip() for l in para_lines)
        # Handle bold
        text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
        content.append({
            "type": "paragraph",
            "content": [{"type": "text", "text": text}],
        })

    return {"type": "doc", "content": content}


def create_draft(subdomain, cookie, title, body_json, subtitle=""):
    resp = requests.post(
        f"https://{subdomain}.substack.com/api/v1/drafts",
        cookies={"substack.sid": cookie},
        json={
            "draft_title": title,
            "draft_subtitle": subtitle,
            "draft_body": json.dumps(body_json),
            "type": "newsletter",
        },
    )
    resp.raise_for_status()
    return resp.json()


def extract_title(content):
    for line in content.splitlines():
        line = line.strip()
        if line and not line.startswith("![") and not line.startswith("---"):
            return line.lstrip("#").strip().rstrip("=").strip()
    return "Untitled"


def load_publish_log():
    if PUBLISH_LOG.exists():
        return json.loads(PUBLISH_LOG.read_text())
    return {"publications": [], "stats": {"total_published": 0}}


def save_publish_log(log):
    PUBLISH_LOG.write_text(json.dumps(log, ensure_ascii=False, indent=2))


def main():
    parser = argparse.ArgumentParser(description="Publish articles to Substack")
    parser.add_argument("--lang", required=True, help="Language code")
    parser.add_argument("--subdomain", required=True, help="Substack subdomain")
    parser.add_argument("--category", help="Only publish specific category")
    parser.add_argument("--limit", type=int, default=0, help="Max articles")
    parser.add_argument("--delay", type=int, default=10, help="Delay between posts")
    args = parser.parse_args()

    cookie = get_substack_cookie()
    print(f"Using Substack newsletter: {args.subdomain}.substack.com")

    lang_dir = TRANSLATED_DIR / args.lang
    if not lang_dir.exists():
        print(f"No translated files for: {args.lang}")
        return

    log = load_publish_log()
    published_keys = {
        p["source_file"]
        for p in log["publications"]
        if p.get("platform") == "substack"
    }

    md_files = sorted(lang_dir.rglob("*.md"))
    if args.category:
        md_files = [f for f in md_files if args.category in str(f)]

    count = 0
    for md_file in md_files:
        rel_path = str(md_file.relative_to(TRANSLATED_DIR))
        if rel_path in published_keys:
            print(f"  SKIP: {rel_path}")
            continue

        content = md_file.read_text()
        title = extract_title(content)
        body_json = markdown_to_prosemirror(content)

        try:
            result = create_draft(args.subdomain, cookie, title, body_json)
            draft_id = result.get("id", "unknown")
            print(f"  OK (draft): {title} -> id={draft_id}")

            log["publications"].append({
                "source_file": rel_path,
                "platform": "substack",
                "language": args.lang,
                "title": title,
                "substack_draft_id": draft_id,
                "subdomain": args.subdomain,
                "status": "draft",
                "published_at": datetime.now().isoformat(),
            })
            log["stats"]["total_published"] += 1
            log["stats"]["substack_published"] = (
                log["stats"].get("substack_published", 0) + 1
            )
            save_publish_log(log)

            count += 1
            if args.limit and count >= args.limit:
                break

            time.sleep(args.delay)

        except Exception as e:
            print(f"  FAIL: {title} -> {e}")
            log.setdefault("failed_publications", []).append({
                "source_file": rel_path,
                "platform": "substack",
                "error": str(e),
                "timestamp": datetime.now().isoformat(),
            })
            save_publish_log(log)

    print(f"\nDone. Created {count} drafts on Substack.")


if __name__ == "__main__":
    main()
