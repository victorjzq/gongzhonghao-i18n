#!/usr/bin/env python3
"""
fix_internal_links.py — 把关联形态表中的纯文本模块ID转换为 Markdown 链接
用法: python scripts/fix_internal_links.py [--dry-run]
"""

import os
import re
import sys
import yaml
from pathlib import Path

ARTICLES_DIR = Path(__file__).parent.parent / "articles"

def load_article_index():
    """读取所有文章 frontmatter，建立 module_id → [filename] 映射"""
    index = {}  # module_id → [(pattern_id, filename, title)]
    for f in sorted(ARTICLES_DIR.glob("*.md")):
        text = f.read_text(encoding="utf-8")
        # 提取 YAML frontmatter
        m = re.match(r'^---\n(.*?)\n---', text, re.DOTALL)
        if not m:
            continue
        try:
            meta = yaml.safe_load(m.group(1))
        except:
            continue
        if not meta:
            continue
        module_id = meta.get("module_id", "")
        pattern_id = meta.get("pattern_id", "")
        title = meta.get("title", f.stem)
        if module_id:
            index.setdefault(module_id, []).append({
                "pattern_id": pattern_id,
                "filename": f.name,
                "title": title,
            })
    return index


def get_best_link(module_id, index):
    """给定 module_id，返回最佳链接目标（如果多篇文章属于同一模块，选第一篇）"""
    entries = index.get(module_id, [])
    if not entries:
        return None
    # 优先选和 module_id 同名的
    for e in entries:
        if e["pattern_id"] == module_id:
            return e
    return entries[0]


def fix_links_in_file(filepath, index, dry_run=False):
    """修复单个文章中的关联形态表"""
    text = filepath.read_text(encoding="utf-8")

    # 获取当前文章的 module_id，避免自链
    m = re.match(r'^---\n(.*?)\n---', text, re.DOTALL)
    self_module = ""
    if m:
        try:
            meta = yaml.safe_load(m.group(1))
            self_module = meta.get("module_id", "")
        except:
            pass

    changes = 0
    lines = text.split("\n")
    new_lines = []
    in_table = False

    for line in lines:
        # 检测关联形态表
        if "关联模块" in line and "关系" in line and "说明" in line:
            in_table = True
            new_lines.append(line)
            continue

        if in_table:
            # 表格结束检测
            if not line.startswith("|") and line.strip() != "":
                in_table = False
                new_lines.append(line)
                continue
            if line.strip() == "":
                in_table = False
                new_lines.append(line)
                continue

            # 跳过分隔行
            if re.match(r'^\|[-\s|]+\|$', line):
                new_lines.append(line)
                continue

            # 解析表格行: | MODULE_ID | relation | description |
            cells = [c.strip() for c in line.split("|")]
            # cells[0] = '', cells[1] = module_id, cells[2] = relation, cells[3] = desc, cells[4] = ''
            if len(cells) >= 4:
                module_ref = cells[1].strip()
                # 检查是否已经是链接
                if "[" in module_ref:
                    new_lines.append(line)
                    continue
                # 查找链接目标
                target = get_best_link(module_ref, index)
                if target and module_ref != self_module:
                    linked = f"[{module_ref}](./{target['filename']})"
                    cells[1] = f" {linked} "
                    new_line = "|".join(cells)
                    new_lines.append(new_line)
                    changes += 1
                    continue

            new_lines.append(line)
        else:
            new_lines.append(line)

    if changes > 0 and not dry_run:
        filepath.write_text("\n".join(new_lines), encoding="utf-8")

    return changes


def main():
    dry_run = "--dry-run" in sys.argv

    print("=== 文章互链修复工具 ===")
    print(f"目录: {ARTICLES_DIR}")
    print(f"模式: {'DRY RUN' if dry_run else 'WRITE'}")
    print()

    # 1. 建立索引
    index = load_article_index()
    print(f"模块索引: {len(index)} 个模块")
    for mid, entries in sorted(index.items()):
        fnames = [e['filename'] for e in entries]
        print(f"  {mid}: {', '.join(fnames)}")
    print()

    # 2. 修复每篇文章
    total_changes = 0
    files_changed = 0
    for f in sorted(ARTICLES_DIR.glob("*.md")):
        changes = fix_links_in_file(f, index, dry_run)
        if changes > 0:
            print(f"  ✅ {f.name}: {changes} 个链接")
            total_changes += changes
            files_changed += 1
        else:
            print(f"  — {f.name}: 无变更")

    print()
    print(f"=== 总计: {files_changed} 篇文章, {total_changes} 个链接{'（DRY RUN）' if dry_run else '已修复'} ===")


if __name__ == "__main__":
    main()
