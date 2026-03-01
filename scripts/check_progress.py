#!/usr/bin/env python3
"""公众号国际化项目 — 翻译 + 发布进度统计。

用法:
    python check_progress.py              # 终端输出
    python check_progress.py --notify     # 输出 + 发企业微信
    python check_progress.py --json       # JSON 格式输出
"""

import argparse
import json
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
TRANSLATED_DIR = BASE_DIR / "translated"
SOURCE_DIR = BASE_DIR / "公众号文章"
PUBLISH_LOG = BASE_DIR / "logs" / "publish_log.json"

# 目标语言列表
LANGS = ["en", "vi", "ja", "ko", "es", "fr", "de", "pt", "ar", "ru", "id"]
PLATFORMS = ["dev.to", "hashnode", "medium", "substack"]


def count_md_files(directory: Path) -> int:
    """递归统计 .md 文件数量。"""
    if not directory.exists():
        return 0
    return sum(1 for _ in directory.rglob("*.md"))


def load_publish_log() -> list:
    """加载发布日志。"""
    if not PUBLISH_LOG.exists():
        return []
    try:
        data = json.loads(PUBLISH_LOG.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            return data.get("publications", [])
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def get_progress() -> dict:
    """计算完整进度数据。"""
    source_count = count_md_files(SOURCE_DIR) or 351

    # 翻译进度
    translations = {}
    for lang in LANGS:
        lang_dir = TRANSLATED_DIR / lang
        count = count_md_files(lang_dir)
        translations[lang] = {
            "count": count,
            "total": source_count,
            "pct": round(count / source_count * 100, 1) if source_count else 0,
        }

    # 发布进度
    pub_log = load_publish_log()
    publications = {}
    for platform in PLATFORMS:
        count = sum(
            1 for p in pub_log
            if platform in str(p.get("platform", "")) or platform in str(p.get("url", ""))
        )
        publications[platform] = count

    return {
        "source_count": source_count,
        "translations": translations,
        "publications": publications,
        "total_published": len(pub_log),
    }


def format_report(data: dict) -> str:
    """格式化进度报告。"""
    lines = []
    lines.append("=" * 50)
    lines.append("📊 公众号国际化项目进度")
    lines.append("=" * 50)

    lines.append(f"\n📝 翻译进度 (源文件 {data['source_count']} 篇):")
    for lang, info in data["translations"].items():
        count = info["count"]
        pct = info["pct"]
        total = info["total"]
        filled = int(pct / 10)
        bar = "█" * filled + "░" * (10 - filled)
        status = "✅" if pct >= 99 else f"{pct:.0f}%"
        lines.append(f"  {lang:4s}: [{bar}] {count:3d}/{total} {status}")

    lines.append(f"\n📤 发布进度:")
    for platform, count in data["publications"].items():
        lines.append(f"  {platform:12s}: {count} 篇")

    lines.append(f"\n总发布记录: {data['total_published']} 篇")
    lines.append("=" * 50)

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="公众号进度统计")
    parser.add_argument("--notify", action="store_true", help="发送到企业微信")
    parser.add_argument("--json", action="store_true", help="JSON 输出")
    args = parser.parse_args()

    data = get_progress()

    if args.json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
        return

    report = format_report(data)
    print(report)

    if args.notify:
        try:
            sys.path.insert(0, os.path.expanduser("~/Claude-Global/Zoe"))
            from zoe_notify import notify
            notify(report, level="info")
            print("\n✅ 已发送到企业微信")
        except Exception as e:
            print(f"\n❌ 发送失败: {e}")


if __name__ == "__main__":
    main()
