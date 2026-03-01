#!/usr/bin/env python3
"""
修复 publish_log.json 中 source 字段格式不统一的问题。

问题分析：
  - 早期 30 条记录使用 "source" 字段，格式为 "交易书籍/xxx.md"（无 en/ 前缀）
  - 后续 199 条记录使用 "source_file" 字段，格式为 "en/交易书籍/xxx.md"（带 en/ 前缀）

修复策略：
  1. 统一字段名为 "source"
  2. 去掉 en/ 前缀，保留相对路径如 "交易书籍/xxx.md"
  3. 去重：同一 platform + source 只保留最新记录
  4. 备份原文件为 logs/publish_log.backup.json

用法: python scripts/fix_publish_log.py [--dry-run]
"""

import json
import shutil
import argparse
from pathlib import Path
from datetime import datetime


BASE_DIR = Path(__file__).parent.parent
PUBLISH_LOG = BASE_DIR / "logs" / "publish_log.json"
BACKUP_LOG = BASE_DIR / "logs" / "publish_log.backup.json"


def normalize_source(record: dict) -> str:
    """从记录中提取并标准化 source 路径（去掉 en/ 前缀）。"""
    src = record.get("source", "") or record.get("source_file", "")
    # 去掉语言前缀，如 en/, vi/, ja/ 等
    parts = src.split("/", 1)
    if len(parts) == 2 and len(parts[0]) <= 3 and parts[0].isalpha():
        src = parts[1]
    return src


def get_record_time(record: dict) -> str:
    """获取记录的时间戳，用于去重时保留最新的。"""
    return record.get("published_at", "") or record.get("date", "") or ""


def fix_publish_log(dry_run: bool = False):
    if not PUBLISH_LOG.exists():
        print(f"ERROR: {PUBLISH_LOG} not found")
        return

    log = json.loads(PUBLISH_LOG.read_text(encoding="utf-8"))
    pubs = log.get("publications", [])

    # --- 统计修复前状态 ---
    stats = {
        "total_before": len(pubs),
        "had_source_field": 0,
        "had_source_file_field": 0,
        "en_prefix_removed": 0,
        "source_file_renamed": 0,
        "duplicates_removed": 0,
        "total_after": 0,
    }

    # --- Step 1: 标准化每条记录 ---
    for p in pubs:
        if "source" in p and "source_file" not in p:
            stats["had_source_field"] += 1
        elif "source_file" in p:
            stats["had_source_file_field"] += 1

    normalized = []
    for p in pubs:
        new_record = {}
        for k, v in p.items():
            if k == "source_file":
                # 重命名为 source 并去掉 en/ 前缀
                new_record["source"] = normalize_source(p)
                stats["source_file_renamed"] += 1
            elif k == "source":
                norm = normalize_source(p)
                if norm != v:
                    stats["en_prefix_removed"] += 1
                new_record["source"] = norm
            else:
                new_record[k] = v
        normalized.append(new_record)

    # --- Step 2: 去重（同一 platform + source 只保留最新记录）---
    seen = {}  # key -> (index, timestamp)
    for i, p in enumerate(normalized):
        src = p.get("source", "")
        plat = p.get("platform", "")
        key = f"{plat}|{src}"
        ts = get_record_time(p)

        if key in seen:
            prev_i, prev_ts = seen[key]
            if ts >= prev_ts:
                # 当前更新，替换
                stats["duplicates_removed"] += 1
                seen[key] = (i, ts)
            else:
                stats["duplicates_removed"] += 1
        else:
            seen[key] = (i, ts)

    # 保留去重后的记录（按原始顺序）
    keep_indices = set(idx for idx, _ in seen.values())
    deduplicated = [p for i, p in enumerate(normalized) if i in keep_indices]
    stats["total_after"] = len(deduplicated)

    # --- 输出统计 ---
    print("=" * 60)
    print("publish_log.json 修复统计")
    print("=" * 60)
    print(f"  修复前总记录数:         {stats['total_before']}")
    print(f"  使用 source 字段:       {stats['had_source_field']}")
    print(f"  使用 source_file 字段:  {stats['had_source_file_field']}")
    print(f"  source_file -> source:  {stats['source_file_renamed']} 条重命名")
    print(f"  去掉 en/ 前缀:          {stats['en_prefix_removed']} 条")
    print(f"  去重删除:               {stats['duplicates_removed']} 条")
    print(f"  修复后总记录数:         {stats['total_after']}")
    print("=" * 60)

    if dry_run:
        print("\n[DRY RUN] 未写入任何文件。")
        return stats

    # --- Step 3: 备份原文件 ---
    shutil.copy2(PUBLISH_LOG, BACKUP_LOG)
    print(f"\n备份已保存: {BACKUP_LOG}")

    # --- Step 4: 写入修复后的文件 ---
    log["publications"] = deduplicated
    log["metadata"]["updated"] = datetime.now().strftime("%Y-%m-%d")

    # 更新 stats
    log_stats = log.get("stats", {})
    platform_counts = {}
    for p in deduplicated:
        plat = p.get("platform", "unknown")
        platform_counts[plat] = platform_counts.get(plat, 0) + 1

    log_stats["total_published"] = len(deduplicated)
    for plat, count in platform_counts.items():
        log_stats[f"{plat}_published"] = count

    log["stats"] = log_stats

    PUBLISH_LOG.write_text(
        json.dumps(log, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"修复完成: {PUBLISH_LOG}")

    return stats


def main():
    parser = argparse.ArgumentParser(description="修复 publish_log.json 格式问题")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="只统计不修改文件",
    )
    args = parser.parse_args()
    fix_publish_log(dry_run=args.dry_run)


if __name__ == "__main__":
    main()
