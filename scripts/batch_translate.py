#!/usr/bin/env python3
"""Batch translate English articles to multiple languages using Anthropic API."""

import os
import json
import time
import argparse
import anthropic

BASE = "/Users/zhiqiangjia/dev/Claude-Global/公众号国际化"
EN_DIR = f"{BASE}/translated/en"
TRANSLATED_DIR = f"{BASE}/translated"
TERMINOLOGY_FILE = f"{BASE}/terminology/terminology.json"

LANG_CONFIG = {
    "vi": {"name": "Vietnamese"},
    "id": {"name": "Indonesian"},
    "es": {"name": "Spanish"},
    "pt": {"name": "Portuguese"},
    "ja": {"name": "Japanese"},
    "ko": {"name": "Korean"},
    "de": {"name": "German"},
    "ar": {"name": "Arabic"},
    "ru": {"name": "Russian"},
}


def load_terminology(lang_code):
    if not os.path.exists(TERMINOLOGY_FILE):
        return ""
    with open(TERMINOLOGY_FILE, "r") as f:
        terminology = json.load(f)
    lines = []
    for t in terminology.get("terms", []):
        en_term = t.get("en", "")
        lang_term = t.get(lang_code, "")
        if en_term and lang_term:
            lines.append(f"- {en_term} → {lang_term}")
    return "\n".join(lines) if lines else "No specific terminology mappings available."


def get_system_prompt(lang_code):
    lang_name = LANG_CONFIG[lang_code]["name"]
    terminology = load_terminology(lang_code)
    return f"""You are a professional English-to-{lang_name} translator specializing in trading and Price Action content by Al Brooks.

RULES:
1. Translate faithfully - do not add, remove, or modify content
2. Preserve ALL Markdown formatting (headers, bold, italic, lists, links, images)
3. Preserve all image links exactly as-is
4. For Al Brooks specific concepts, keep the English original + {lang_name} annotation in parentheses
5. Use the following mandatory terminology mappings:

{terminology}

6. Output ONLY the translated {lang_name} text, no explanations
7. Keep the same paragraph structure as the original"""


def get_all_categories():
    """Auto-detect all categories from EN directory."""
    if not os.path.exists(EN_DIR):
        return []
    return sorted([d for d in os.listdir(EN_DIR)
                   if os.path.isdir(f"{EN_DIR}/{d}")])


def get_files_needing_translation(category, lang_code):
    """Get files that exist in EN but not yet translated."""
    en_path = f"{EN_DIR}/{category}"
    lang_dir = f"{TRANSLATED_DIR}/{lang_code}/{category}"
    os.makedirs(lang_dir, exist_ok=True)

    if not os.path.exists(en_path):
        return []

    needs = []
    for f in sorted(os.listdir(en_path)):
        if not f.endswith(".md"):
            continue
        lang_file = f"{lang_dir}/{f}"
        # Skip if already translated (non-empty, >200 bytes)
        if os.path.exists(lang_file) and os.path.getsize(lang_file) >= 200:
            continue
        needs.append(f)

    return needs


def translate_file(category, filename, lang_code, system_prompt):
    en_file = f"{EN_DIR}/{category}/{filename}"
    lang_dir = f"{TRANSLATED_DIR}/{lang_code}/{category}"
    lang_file = f"{lang_dir}/{filename}"

    with open(en_file, "r") as f:
        content = f.read()

    if len(content.strip()) < 10:
        with open(lang_file, "w") as f:
            f.write(content)
        return True

    client = anthropic.Anthropic()
    lang_name = LANG_CONFIG[lang_code]["name"]

    try:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=8192,
            system=system_prompt,
            messages=[{"role": "user",
                       "content": f"Translate the following English article to {lang_name}:\n\n{content}"}]
        )
        with open(lang_file, "w") as f:
            f.write(response.content[0].text)
        return True
    except Exception as e:
        print(f"  ERROR: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Batch translate articles")
    parser.add_argument("--lang", required=True, choices=list(LANG_CONFIG.keys()))
    parser.add_argument("--batch-size", type=int, default=10)
    parser.add_argument("--max", type=int, default=None, help="Max articles to translate this run")
    parser.add_argument("--category", default=None, help="Only translate specific category")
    args = parser.parse_args()

    lang_code = args.lang
    lang_name = LANG_CONFIG[lang_code]["name"]
    system_prompt = get_system_prompt(lang_code)

    categories = [args.category] if args.category else get_all_categories()

    total_translated = 0
    total_failed = 0
    total_skipped = 0

    print(f"=== Translating to {lang_name} ({lang_code}) ===")
    print(f"Categories: {len(categories)}")
    print()

    for cat in categories:
        files = get_files_needing_translation(cat, lang_code)
        en_count = len([f for f in os.listdir(f"{EN_DIR}/{cat}") if f.endswith(".md")])
        done_count = en_count - len(files)

        if not files:
            print(f"  {cat}: {en_count}/{en_count} ✅")
            total_skipped += en_count
            continue

        print(f"\n{'='*60}")
        print(f"  {cat}: {done_count}/{en_count} done, {len(files)} remaining")
        print(f"{'='*60}")

        for i, f in enumerate(files):
            if args.max and (total_translated + total_failed) >= args.max:
                print(f"\n  Reached --max {args.max}, stopping.")
                break

            print(f"  [{i+1}/{len(files)}] {f[:50]}...", end=" ", flush=True)

            success = translate_file(cat, f, lang_code, system_prompt)
            if success:
                print("✅")
                total_translated += 1
            else:
                print("❌")
                total_failed += 1

            if (i + 1) % args.batch_size == 0:
                print(f"  [Batch {(i+1)//args.batch_size} done, cooling...]")
                time.sleep(2)
            else:
                time.sleep(0.5)

    print(f"\n\n{'='*60}")
    print(f"Done! Translated: {total_translated} | Failed: {total_failed}")
    print(f"{'='*60}")

    # Summary per category
    for cat in categories:
        lang_path = f"{TRANSLATED_DIR}/{lang_code}/{cat}"
        en_count = len([f for f in os.listdir(f"{EN_DIR}/{cat}") if f.endswith(".md")])
        lang_count = len([f for f in os.listdir(lang_path) if f.endswith(".md")]) if os.path.exists(lang_path) else 0
        pct = f"{lang_count/en_count*100:.0f}%" if en_count else "0%"
        print(f"  {cat}: {lang_count}/{en_count} ({pct})")


if __name__ == "__main__":
    main()
