#!/usr/bin/env python3
"""Batch translate English articles to Vietnamese using Anthropic API."""

import os
import json
import time
import anthropic

BASE = "/Users/zhiqiangjia/Claude-Global/公众号国际化"
EN_DIR = f"{BASE}/translated/en"
VI_DIR = f"{BASE}/translated/vi"
TERMINOLOGY_FILE = f"{BASE}/terminology/terminology.json"

# Load terminology
with open(TERMINOLOGY_FILE, "r") as f:
    terminology = json.load(f)

# Build terminology prompt section
term_lines = []
for t in terminology["terms"]:
    en_term = t.get("en", "")
    vi_term = t.get("vi", "")
    if en_term and vi_term:
        term_lines.append(f"- {en_term} → {vi_term}")

TERMINOLOGY_PROMPT = "\n".join(term_lines)

SYSTEM_PROMPT = f"""You are a professional English-to-Vietnamese translator specializing in trading and Price Action content by Al Brooks.

RULES:
1. Translate faithfully - do not add, remove, or modify content
2. Preserve ALL Markdown formatting (headers, bold, italic, lists, links, images)
3. Preserve all image links exactly as-is
4. For Al Brooks specific concepts, keep the English original + Vietnamese annotation in parentheses
5. Use the following mandatory terminology mappings:

{TERMINOLOGY_PROMPT}

6. Output ONLY the translated Vietnamese text, no explanations
7. Keep the same paragraph structure as the original"""


def get_files_needing_translation(category):
    """Get list of files that need translation."""
    en_path = f"{EN_DIR}/{category}"
    vi_path = f"{VI_DIR}/{category}"
    os.makedirs(vi_path, exist_ok=True)

    en_files = set(os.listdir(en_path))
    needs = []
    for f in sorted(en_files):
        if not f.endswith(".md"):
            continue
        vi_file = f"{vi_path}/{f}"
        if not os.path.exists(vi_file) or os.path.getsize(vi_file) < 200:
            needs.append(f)
    return needs


def translate_file(category, filename):
    """Translate a single file."""
    en_file = f"{EN_DIR}/{category}/{filename}"
    vi_file = f"{VI_DIR}/{category}/{filename}"

    with open(en_file, "r") as f:
        content = f.read()

    if len(content.strip()) < 10:
        # Very short file, just copy
        with open(vi_file, "w") as f:
            f.write(content)
        return True

    client = anthropic.Anthropic()

    try:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=8192,
            system=SYSTEM_PROMPT,
            messages=[
                {
                    "role": "user",
                    "content": f"Translate the following English article to Vietnamese:\n\n{content}"
                }
            ]
        )

        translated = response.content[0].text

        with open(vi_file, "w") as f:
            f.write(translated)

        return True
    except Exception as e:
        print(f"  ERROR: {e}")
        return False


def main():
    categories = ["其他概念", "心理与错误"]

    for cat in categories:
        files = get_files_needing_translation(cat)
        print(f"\n{'='*60}")
        print(f"Category: {cat} - {len(files)} files to translate")
        print(f"{'='*60}")

        for i, f in enumerate(files):
            print(f"  [{i+1}/{len(files)}] Translating: {f}...", end=" ", flush=True)
            success = translate_file(cat, f)
            if success:
                print("OK")
            else:
                print("FAILED")
            # Small delay to avoid rate limiting
            time.sleep(0.5)

    print("\n\nDone! Checking results...")
    for cat in categories:
        en_count = len([f for f in os.listdir(f"{EN_DIR}/{cat}") if f.endswith(".md")])
        vi_count = len([f for f in os.listdir(f"{VI_DIR}/{cat}") if f.endswith(".md")])
        small = len([f for f in os.listdir(f"{VI_DIR}/{cat}")
                     if f.endswith(".md") and os.path.getsize(f"{VI_DIR}/{cat}/{f}") < 200])
        print(f"  {cat}: EN={en_count}, VI={vi_count}, small_files={small}")


if __name__ == "__main__":
    main()
