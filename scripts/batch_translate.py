#!/usr/bin/env python3
"""Batch translate English articles to multiple languages using Anthropic API."""

import os
import json
import time
import argparse
import sys
import anthropic

BASE = "/Users/zhiqiangjia/Claude-Global/公众号国际化"
EN_DIR = f"{BASE}/translated/en"
TRANSLATED_DIR = f"{BASE}/translated"
TERMINOLOGY_FILE = f"{BASE}/terminology/terminology.json"

# Language configurations
LANG_CONFIG = {
    "vi": {
        "name": "Vietnamese",
        "system_prompt_template": """You are a professional English-to-Vietnamese translator specializing in trading and Price Action content by Al Brooks.

RULES:
1. Translate faithfully - do not add, remove, or modify content
2. Preserve ALL Markdown formatting (headers, bold, italic, lists, links, images)
3. Preserve all image links exactly as-is
4. For Al Brooks specific concepts, keep the English original + Vietnamese annotation in parentheses
5. Use the following mandatory terminology mappings:

{terminology_prompt}

6. Output ONLY the translated Vietnamese text, no explanations
7. Keep the same paragraph structure as the original"""
    },
    "id": {
        "name": "Indonesian",
        "system_prompt_template": """You are a professional English-to-Indonesian translator specializing in trading and Price Action content by Al Brooks.

RULES:
1. Translate faithfully - do not add, remove, or modify content
2. Preserve ALL Markdown formatting (headers, bold, italic, lists, links, images)
3. Preserve all image links exactly as-is
4. For Al Brooks specific concepts, keep the English original + Indonesian annotation in parentheses
5. Use the following mandatory terminology mappings:

{terminology_prompt}

6. Output ONLY the translated Indonesian text, no explanations
7. Keep the same paragraph structure as the original"""
    },
    "es": {
        "name": "Spanish",
        "system_prompt_template": """You are a professional English-to-Spanish translator specializing in trading and Price Action content by Al Brooks.

RULES:
1. Translate faithfully - do not add, remove, or modify content
2. Preserve ALL Markdown formatting (headers, bold, italic, lists, links, images)
3. Preserve all image links exactly as-is
4. For Al Brooks specific concepts, keep the English original + Spanish annotation in parentheses
5. Use the following mandatory terminology mappings:

{terminology_prompt}

6. Output ONLY the translated Spanish text, no explanations
7. Keep the same paragraph structure as the original"""
    },
    "pt": {
        "name": "Portuguese",
        "system_prompt_template": """You are a professional English-to-Portuguese translator specializing in trading and Price Action content by Al Brooks.

RULES:
1. Translate faithfully - do not add, remove, or modify content
2. Preserve ALL Markdown formatting (headers, bold, italic, lists, links, images)
3. Preserve all image links exactly as-is
4. For Al Brooks specific concepts, keep the English original + Portuguese annotation in parentheses
5. Use the following mandatory terminology mappings:

{terminology_prompt}

6. Output ONLY the translated Portuguese text, no explanations
7. Keep the same paragraph structure as the original"""
    },
    "ja": {
        "name": "Japanese",
        "system_prompt_template": """You are a professional English-to-Japanese translator specializing in trading and Price Action content by Al Brooks.

RULES:
1. Translate faithfully - do not add, remove, or modify content
2. Preserve ALL Markdown formatting (headers, bold, italic, lists, links, images)
3. Preserve all image links exactly as-is
4. For Al Brooks specific concepts, keep the English original + Japanese annotation in parentheses
5. Use the following mandatory terminology mappings:

{terminology_prompt}

6. Output ONLY the translated Japanese text, no explanations
7. Keep the same paragraph structure as the original"""
    },
    "ko": {
        "name": "Korean",
        "system_prompt_template": """You are a professional English-to-Korean translator specializing in trading and Price Action content by Al Brooks.

RULES:
1. Translate faithfully - do not add, remove, or modify content
2. Preserve ALL Markdown formatting (headers, bold, italic, lists, links, images)
3. Preserve all image links exactly as-is
4. For Al Brooks specific concepts, keep the English original + Korean annotation in parentheses
5. Use the following mandatory terminology mappings:

{terminology_prompt}

6. Output ONLY the translated Korean text, no explanations
7. Keep the same paragraph structure as the original"""
    },
    "de": {
        "name": "German",
        "system_prompt_template": """You are a professional English-to-German translator specializing in trading and Price Action content by Al Brooks.

RULES:
1. Translate faithfully - do not add, remove, or modify content
2. Preserve ALL Markdown formatting (headers, bold, italic, lists, links, images)
3. Preserve all image links exactly as-is
4. For Al Brooks specific concepts, keep the English original + German annotation in parentheses
5. Use the following mandatory terminology mappings:

{terminology_prompt}

6. Output ONLY the translated German text, no explanations
7. Keep the same paragraph structure as the original"""
    },
    "ar": {
        "name": "Arabic",
        "system_prompt_template": """You are a professional English-to-Arabic translator specializing in trading and Price Action content by Al Brooks.

RULES:
1. Translate faithfully - do not add, remove, or modify content
2. Preserve ALL Markdown formatting (headers, bold, italic, lists, links, images)
3. Preserve all image links exactly as-is
4. For Al Brooks specific concepts, keep the English original + Arabic annotation in parentheses
5. Use the following mandatory terminology mappings:

{terminology_prompt}

6. Output ONLY the translated Arabic text, no explanations
7. Keep the same paragraph structure as the original"""
    },
    "ru": {
        "name": "Russian",
        "system_prompt_template": """You are a professional English-to-Russian translator specializing in trading and Price Action content by Al Brooks.

RULES:
1. Translate faithfully - do not add, remove, or modify content
2. Preserve ALL Markdown formatting (headers, bold, italic, lists, links, images)
3. Preserve all image links exactly as-is
4. For Al Brooks specific concepts, keep the English original + Russian annotation in parentheses
5. Use the following mandatory terminology mappings:

{terminology_prompt}

6. Output ONLY the translated Russian text, no explanations
7. Keep the same paragraph structure as the original"""
    }
}


def load_terminology(lang_code):
    """Load and format terminology for specific language."""
    with open(TERMINOLOGY_FILE, "r") as f:
        terminology = json.load(f)

    term_lines = []
    for t in terminology["terms"]:
        en_term = t.get("en", "")
        lang_term = t.get(lang_code, "")
        if en_term and lang_term:
            term_lines.append(f"- {en_term} → {lang_term}")

    return "\n".join(term_lines)


def get_system_prompt(lang_code):
    """Build system prompt for specific language."""
    if lang_code not in LANG_CONFIG:
        raise ValueError(f"Unsupported language: {lang_code}")

    terminology_prompt = load_terminology(lang_code)
    template = LANG_CONFIG[lang_code]["system_prompt_template"]
    return template.format(terminology_prompt=terminology_prompt)


def get_article_number(filename):
    """Extract article number from filename (e.g., '041_some_title.md' -> 41)."""
    try:
        return int(filename.split("_")[0])
    except (ValueError, IndexError):
        return None


def get_files_needing_translation(category, lang_code, start=41, end=None):
    """Get list of files that need translation."""
    en_path = f"{EN_DIR}/{category}"
    lang_dir = f"{TRANSLATED_DIR}/{lang_code}/{category}"
    os.makedirs(lang_dir, exist_ok=True)

    if not os.path.exists(en_path):
        return []

    en_files = set(os.listdir(en_path))
    needs = []

    for f in sorted(en_files):
        if not f.endswith(".md"):
            continue

        article_num = get_article_number(f)
        if article_num is None:
            continue

        # Filter by range
        if article_num < start:
            continue
        if end is not None and article_num > end:
            continue

        lang_file = f"{lang_dir}/{f}"
        # Skip if already translated (and non-empty)
        if os.path.exists(lang_file) and os.path.getsize(lang_file) >= 200:
            continue

        needs.append(f)

    return needs


def translate_file(category, filename, lang_code, system_prompt):
    """Translate a single file."""
    en_file = f"{EN_DIR}/{category}/{filename}"
    lang_dir = f"{TRANSLATED_DIR}/{lang_code}/{category}"
    lang_file = f"{lang_dir}/{filename}"

    with open(en_file, "r") as f:
        content = f.read()

    if len(content.strip()) < 10:
        # Very short file, just copy
        with open(lang_file, "w") as f:
            f.write(content)
        return True

    client = anthropic.Anthropic()

    try:
        lang_name = LANG_CONFIG[lang_code]["name"]
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=8192,
            system=system_prompt,
            messages=[
                {
                    "role": "user",
                    "content": f"Translate the following English article to {lang_name}:\n\n{content}"
                }
            ]
        )

        translated = response.content[0].text

        with open(lang_file, "w") as f:
            f.write(translated)

        return True
    except Exception as e:
        print(f"  ERROR: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Batch translate articles to multiple languages")
    parser.add_argument("--lang", required=True, choices=list(LANG_CONFIG.keys()),
                       help="Target language code (vi/id/es/pt/ja/ko/de/ar/ru)")
    parser.add_argument("--start", type=int, default=41,
                       help="Start article number (default: 41)")
    parser.add_argument("--end", type=int, default=None,
                       help="End article number (default: None, no limit)")
    parser.add_argument("--batch-size", type=int, default=10,
                       help="Batch size for processing (default: 10)")

    args = parser.parse_args()

    lang_code = args.lang
    lang_name = LANG_CONFIG[lang_code]["name"]

    categories = ["其他概念", "心理与错误"]
    system_prompt = get_system_prompt(lang_code)

    total_translated = 0
    total_failed = 0

    for cat in categories:
        files = get_files_needing_translation(cat, lang_code, args.start, args.end)

        if not files:
            print(f"Category: {cat} - No files to translate")
            continue

        print(f"\n{'='*60}")
        print(f"Category: {cat} ({lang_name}) - {len(files)} files to translate")
        print(f"Range: {args.start}-{args.end if args.end else 'end'}")
        print(f"{'='*60}")

        for i, f in enumerate(files):
            article_num = get_article_number(f)
            print(f"  [{i+1}/{len(files)}] [{article_num:03d}] {f}...", end=" ", flush=True)

            success = translate_file(cat, f, lang_code, system_prompt)
            if success:
                print("OK")
                total_translated += 1
            else:
                print("FAILED")
                total_failed += 1

            # Rate limiting
            if (i + 1) % args.batch_size == 0:
                print(f"  [Batch complete, sleeping...]")
                time.sleep(2)
            else:
                time.sleep(0.5)

    print("\n\nDone! Results:")
    print(f"  Total translated: {total_translated}")
    print(f"  Total failed: {total_failed}")

    for cat in categories:
        lang_path = f"{TRANSLATED_DIR}/{lang_code}/{cat}"
        if os.path.exists(lang_path):
            en_count = len([f for f in os.listdir(f"{EN_DIR}/{cat}") if f.endswith(".md")])
            lang_count = len([f for f in os.listdir(lang_path) if f.endswith(".md")])
            small = len([f for f in os.listdir(lang_path)
                        if f.endswith(".md") and os.path.getsize(f"{lang_path}/{f}") < 200])
            print(f"  {cat}: EN={en_count}, {lang_code.upper()}={lang_count}, small_files={small}")


if __name__ == "__main__":
    main()
