#!/usr/bin/env python3
"""
批量发布 translated/en/ 下未发布的文章到 Dev.to。

功能：
  - 读取 translated/en/ 目录下所有 .md 文章
  - 对比 logs/publish_log.json，找出未发布到 devto 的文章
  - 使用 DEV_TO_API_KEY 环境变量或 .env 文件中的 key
  - 每篇发布间隔 120 秒（避免 429 限流）
  - 429 时 backoff 重试（60s / 120s / 180s）
  - 发布成功后实时写入 publish_log.json
  - 支持 --dry-run 参数只统计不发布
  - 支持 --limit N 参数限制发布数量

用法:
  python scripts/batch_publish_devto.py --dry-run          # 只统计
  python scripts/batch_publish_devto.py --limit 5          # 发布 5 篇
  python scripts/batch_publish_devto.py                    # 发布全部未发布文章
  python scripts/batch_publish_devto.py --category 交易书籍 # 只发布特定分类
"""

import os
import json
import time
import argparse
import requests
from pathlib import Path
from datetime import datetime


# --- 路径配置 ---
BASE_DIR = Path(__file__).parent.parent
TRANSLATED_EN_DIR = BASE_DIR / "translated" / "en"
LOGS_DIR = BASE_DIR / "logs"
PUBLISH_LOG = LOGS_DIR / "publish_log.json"

DEVTO_API_BASE = "https://dev.to/api"
PUBLISH_DELAY = 120  # 秒
BACKOFF_SCHEDULE = [60, 120, 180]  # 429 重试等待秒数

DEVTO_TAGS = ["priceaction", "trading", "albrooks", "technicalanalysis"]


# --- 异常 ---
class RateLimitError(Exception):
    pass


# --- API Key ---
def get_devto_key() -> str:
    """从环境变量或 .env 文件获取 Dev.to API Key。"""
    key = os.environ.get("DEVTO_API_KEY") or os.environ.get("DEV_TO_API_KEY")
    if key:
        return key

    env_file = BASE_DIR / ".env"
    if env_file.exists():
        for line in env_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("DEVTO_API_KEY=") or line.startswith("DEV_TO_API_KEY="):
                key = line.split("=", 1)[1].strip().strip('"').strip("'")
                if key and not key.startswith("your_"):
                    return key

    raise ValueError(
        "DEVTO_API_KEY not found.\n"
        "Set it via: export DEVTO_API_KEY=xxx\n"
        "Or add to .env: DEVTO_API_KEY=xxx"
    )


# --- 标题提取 ---
def extract_title(content: str) -> str:
    """从 Markdown 内容提取标题。"""
    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("#") and not stripped.startswith("#!"):
            title = stripped.lstrip("#").strip()
            if title:
                return title[:120]
    # fallback: 第一个非空、非图片行
    for line in content.splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("![") and not stripped.startswith("---"):
            title = stripped.lstrip("#").strip().replace("**", "")
            return title[:120] if title else "Untitled"
    return "Untitled"


# --- Publish Log ---
def load_publish_log() -> dict:
    """加载 publish_log.json。"""
    if PUBLISH_LOG.exists():
        return json.loads(PUBLISH_LOG.read_text(encoding="utf-8"))
    return {
        "metadata": {
            "created": datetime.now().strftime("%Y-%m-%d"),
            "updated": datetime.now().strftime("%Y-%m-%d"),
            "platforms": ["devto"],
            "languages": ["en"],
        },
        "publications": [],
        "stats": {"total_published": 0, "devto_published": 0},
    }


def save_publish_log(log: dict):
    """实时写入 publish_log.json。"""
    log["metadata"]["updated"] = datetime.now().strftime("%Y-%m-%d")
    PUBLISH_LOG.write_text(
        json.dumps(log, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def get_published_devto_sources(log: dict) -> set:
    """
    获取已发布到 devto 的 source 集合。
    兼容新旧两种字段格式（source / source_file，有无 en/ 前缀）。
    """
    sources = set()
    for p in log.get("publications", []):
        if p.get("platform") != "devto":
            continue
        src = p.get("source", "") or p.get("source_file", "")
        # 标准化：去掉语言前缀
        parts = src.split("/", 1)
        if len(parts) == 2 and len(parts[0]) <= 3 and parts[0].isalpha():
            src = parts[1]
        sources.add(src)
    return sources


# --- Dev.to API ---
def publish_to_devto(
    api_key: str, title: str, body_markdown: str, tags: list, published: bool = True
) -> dict:
    """发布一篇文章到 Dev.to，返回 API 响应。"""
    resp = requests.post(
        f"{DEVTO_API_BASE}/articles",
        headers={
            "api-key": api_key,
            "Content-Type": "application/json",
        },
        json={
            "article": {
                "title": title,
                "body_markdown": body_markdown,
                "tags": tags[:4],  # Dev.to 最多 4 个 tag
                "published": published,
            }
        },
        timeout=30,
    )

    if resp.status_code == 429:
        raise RateLimitError("429 Too Many Requests")

    resp.raise_for_status()
    return resp.json()


def publish_with_backoff(
    api_key: str, title: str, body_markdown: str, tags: list, published: bool = True
) -> dict | None:
    """带 backoff 重试的发布，429 时按 60s/120s/180s 重试。"""
    for attempt, wait_time in enumerate(BACKOFF_SCHEDULE):
        try:
            return publish_to_devto(api_key, title, body_markdown, tags, published)
        except RateLimitError:
            print(f"    429 RATE LIMITED: waiting {wait_time}s (attempt {attempt + 1}/{len(BACKOFF_SCHEDULE)})...")
            time.sleep(wait_time)
        except requests.exceptions.HTTPError as e:
            print(f"    HTTP ERROR: {e}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"    REQUEST ERROR: {e}")
            return None

    # 所有重试都失败
    print(f"    GIVING UP after {len(BACKOFF_SCHEDULE)} retries")
    return None


# --- 收集未发布文章 ---
def collect_unpublished_articles(
    published_sources: set, category: str | None = None
) -> list[tuple[Path, str]]:
    """
    扫描 translated/en/ 下所有 .md 文件，返回未发布的 (文件路径, 相对source路径) 列表。
    """
    unpublished = []
    for md_file in sorted(TRANSLATED_EN_DIR.rglob("*.md")):
        # 相对于 translated/en/ 的路径，如 "交易书籍/xxx.md"
        rel_source = str(md_file.relative_to(TRANSLATED_EN_DIR))

        if category and category not in rel_source:
            continue

        if rel_source not in published_sources:
            unpublished.append((md_file, rel_source))

    return unpublished


# --- 主流程 ---
def main():
    parser = argparse.ArgumentParser(
        description="批量发布 translated/en/ 下未发布的文章到 Dev.to"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="只统计不发布，输出待发布文章列表",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="限制发布数量（0 = 不限制）",
    )
    parser.add_argument(
        "--category",
        type=str,
        default=None,
        help="只发布特定分类目录下的文章（如 '交易书籍'）",
    )
    parser.add_argument(
        "--delay",
        type=int,
        default=PUBLISH_DELAY,
        help=f"发布间隔秒数（默认 {PUBLISH_DELAY}）",
    )
    parser.add_argument(
        "--draft",
        action="store_true",
        help="以草稿模式发布（不公开）",
    )
    args = parser.parse_args()

    # 加载日志
    log = load_publish_log()
    published_sources = get_published_devto_sources(log)

    # 收集未发布文章
    unpublished = collect_unpublished_articles(published_sources, args.category)

    # 应用 limit
    if args.limit > 0:
        unpublished = unpublished[: args.limit]

    # --- 统计输出 ---
    total_en = sum(1 for _ in TRANSLATED_EN_DIR.rglob("*.md"))
    print("=" * 60)
    print("Dev.to 批量发布统计")
    print("=" * 60)
    print(f"  translated/en/ 总文章数:  {total_en}")
    print(f"  已发布到 devto:           {len(published_sources)}")
    print(f"  待发布:                   {len(unpublished)}")
    if args.category:
        print(f"  筛选分类:                 {args.category}")
    if args.limit > 0:
        print(f"  本次限制:                 {args.limit} 篇")
    print("=" * 60)

    if not unpublished:
        print("\n所有文章都已发布，无需操作。")
        return

    # --- dry-run 模式 ---
    if args.dry_run:
        print("\n[DRY RUN] 待发布文章列表:")
        for i, (md_file, rel_source) in enumerate(unpublished, 1):
            content = md_file.read_text(encoding="utf-8")
            title = extract_title(content)
            print(f"  {i:3d}. [{rel_source}]")
            print(f"       {title}")
        print(f"\n[DRY RUN] 共 {len(unpublished)} 篇待发布，未执行任何操作。")
        return

    # --- 实际发布 ---
    api_key = get_devto_key()
    published_flag = not args.draft
    mode = "public" if published_flag else "draft"
    print(f"\n开始发布（模式: {mode}，间隔: {args.delay}s）...\n")

    success_count = 0
    fail_count = 0

    for i, (md_file, rel_source) in enumerate(unpublished, 1):
        content = md_file.read_text(encoding="utf-8")
        title = extract_title(content)

        print(f"[{i}/{len(unpublished)}] {rel_source}")
        print(f"  Title: {title}")

        result = publish_with_backoff(
            api_key, title, content, DEVTO_TAGS, published=published_flag
        )

        if result:
            url = result.get("url", "")
            article_id = result.get("id", "")
            print(f"  OK -> {url}")

            # 实时写入日志
            log["publications"].append(
                {
                    "date": datetime.now().strftime("%Y-%m-%d"),
                    "platform": "devto",
                    "language": "en",
                    "source": rel_source,
                    "title": title,
                    "url": url,
                    "article_id": article_id,
                    "status": "published" if published_flag else "draft",
                    "published_at": datetime.now().isoformat(),
                }
            )

            # 更新 stats
            log_stats = log.setdefault("stats", {})
            log_stats["total_published"] = log_stats.get("total_published", 0) + 1
            log_stats["devto_published"] = log_stats.get("devto_published", 0) + 1

            save_publish_log(log)
            success_count += 1
        else:
            print(f"  FAIL")

            # 记录失败
            log.setdefault("failed_publications", []).append(
                {
                    "source": rel_source,
                    "platform": "devto",
                    "error": "publish failed after retries",
                    "timestamp": datetime.now().isoformat(),
                }
            )
            save_publish_log(log)
            fail_count += 1

        # 间隔等待（最后一篇不等待）
        if i < len(unpublished):
            print(f"  Waiting {args.delay}s...")
            time.sleep(args.delay)

    # --- 最终统计 ---
    print("\n" + "=" * 60)
    print("发布完成")
    print("=" * 60)
    print(f"  成功: {success_count}")
    print(f"  失败: {fail_count}")
    print(f"  总计: {success_count + fail_count}")
    print("=" * 60)


if __name__ == "__main__":
    main()
