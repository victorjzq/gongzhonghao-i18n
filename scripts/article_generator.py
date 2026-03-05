#!/usr/bin/env python3
"""
Article Generator v1 — JSON → Jinja2 Markdown 骨架

Pipeline: DataLoader → ClusterRouter → PromptBuilder → SEOOptimizer → .md
"""

import json
import re
import unicodedata
from datetime import datetime
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

# ─── 路径 ───────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent.parent
KNOWLEDGE_DIR = Path.home() / ".claude" / "knowledge" / "brooks-encyclopedia"
TEMPLATE_DIR = PROJECT_ROOT / "templates"
OUTPUT_DIR = PROJECT_ROOT / "articles"


# ═══════════════════════════════════════════════════════════
# 1. DataLoader
# ═══════════════════════════════════════════════════════════
class DataLoader:
    """读取 ~/.claude/knowledge/brooks-encyclopedia/M*.json"""

    def __init__(self, knowledge_dir: Path = KNOWLEDGE_DIR):
        self.knowledge_dir = knowledge_dir

    def load_module(self, filename: str) -> dict:
        path = self.knowledge_dir / filename
        with open(path, encoding="utf-8") as f:
            return json.load(f)

    def load_all_modules(self) -> list[dict]:
        modules = []
        for p in sorted(self.knowledge_dir.glob("M*.json")):
            with open(p, encoding="utf-8") as f:
                modules.append(json.load(f))
        return modules

    def get_pattern(self, module_data: dict, pattern_id: str) -> dict | None:
        for p in module_data.get("patterns", []):
            if p["pattern_id"] == pattern_id:
                return p
        return None


# ═══════════════════════════════════════════════════════════
# 2. ClusterRouter
# ═══════════════════════════════════════════════════════════
CLUSTER_MAP = {
    "M1_MTR": {"id": 1, "name": "PA基础", "slug_prefix": "price-action-basics"},
    "M2_SPIKE_CHANNEL": {"id": 3, "name": "视觉模式", "slug_prefix": "visual-patterns"},
    "M3_TRADING_RANGE": {"id": 3, "name": "视觉模式", "slug_prefix": "visual-patterns"},
    "M4_MEASURED_MOVE": {"id": 4, "name": "交易管理", "slug_prefix": "trade-management"},
    "M5_SIGNAL_BAR": {"id": 2, "name": "Brooks方法论", "slug_prefix": "brooks-methodology"},
    "M6_ENTRY_EXIT": {"id": 2, "name": "Brooks方法论", "slug_prefix": "brooks-methodology"},
    "M7_HIGH2": {"id": 2, "name": "Brooks方法论", "slug_prefix": "brooks-methodology"},
    "M8_UNIFIED": {"id": 5, "name": "跨资产应用", "slug_prefix": "cross-asset"},
}


class ClusterRouter:
    """按 module_id 映射到 5 大支柱集群"""

    def route(self, module_id: str) -> dict:
        return CLUSTER_MAP.get(module_id, {"id": 0, "name": "未分类", "slug_prefix": "misc"})


# ═══════════════════════════════════════════════════════════
# 3. SEOOptimizer
# ═══════════════════════════════════════════════════════════
class SEOOptimizer:
    """Title < 60字符检查 + slug 自动生成"""

    MAX_TITLE_LEN = 60

    # 模式 → SEO 标题映射（可扩展）
    TITLE_TEMPLATES = {
        "H2_BULL_FLAG": "1个高胜率H2看涨形态：告别踏空单边趋势的交易秘籍",
        "L2_BEAR_FLAG": "1个高胜率L2看跌形态：精准捕捉空头趋势的做空指南",
    }

    META_TEMPLATES = {
        "H2_BULL_FLAG": "深度解析 Al Brooks PA 中的 H2 Bull 形态。掌握入场规则、止损逻辑与胜率数据。",
        "L2_BEAR_FLAG": "深度解析 Al Brooks PA 中的 L2 Bear 形态。掌握做空入场、止损逻辑与胜率数据。",
    }

    def generate_title(self, pattern: dict) -> str:
        title = self.TITLE_TEMPLATES.get(pattern["pattern_id"], pattern["name"])
        if len(title) > self.MAX_TITLE_LEN:
            title = title[: self.MAX_TITLE_LEN - 1] + "…"
        return title

    def generate_slug(self, cluster_prefix: str, pattern: dict) -> str:
        raw = pattern["pattern_id"].lower().replace("_", "-")
        slug = f"/{cluster_prefix}/{raw}-guide"
        return slug

    def generate_meta(self, pattern: dict) -> str:
        return self.META_TEMPLATES.get(
            pattern["pattern_id"],
            f"深度解析 Al Brooks PA 中的 {pattern['name']}。完整规则、胜率数据与实战技巧。",
        )

    def validate_title(self, title: str) -> bool:
        return len(title) <= self.MAX_TITLE_LEN


# ═══════════════════════════════════════════════════════════
# 4. PromptBuilder
# ═══════════════════════════════════════════════════════════

# H2_BULL 的概率表（来自设计文档）
PROBABILITY_TABLES = {
    "H2_BULL_FLAG": [
        {"style": "顺势短线", "context": "强多头趋势小幅回调", "win_rate": "60%-70%", "rr": "1:1"},
        {"style": "波段交易", "context": "EMA附近深度回调", "win_rate": "40%-50%", "rr": "2:1+"},
        {"style": "逆势交易", "context": "熊势反弹", "win_rate": "<30%", "rr": "不建议"},
    ],
    "L2_BEAR_FLAG": [
        {"style": "顺势短线", "context": "强空头趋势小幅反弹", "win_rate": "60%-70%", "rr": "1:1"},
        {"style": "波段交易", "context": "EMA附近深度反弹", "win_rate": "40%-50%", "rr": "2:1+"},
        {"style": "逆势交易", "context": "牛势回调", "win_rate": "<30%", "rr": "不建议"},
    ],
}


class PromptBuilder:
    """Jinja2 模板渲染 → Markdown 骨架"""

    def __init__(self, template_dir: Path = TEMPLATE_DIR):
        self.env = Environment(
            loader=FileSystemLoader(str(template_dir)),
            keep_trailing_newline=True,
            trim_blocks=True,
            lstrip_blocks=True,
        )
        self.template = self.env.get_template("article.md.j2")

    def render(
        self,
        module_data: dict,
        pattern: dict,
        cluster: dict,
        seo: dict,
        cross_references: list | None = None,
    ) -> str:
        return self.template.render(
            module=module_data,
            pattern=pattern,
            cluster=cluster,
            seo=seo,
            cross_references=cross_references or module_data.get("cross_references", []),
            probability_table=PROBABILITY_TABLES.get(pattern["pattern_id"]),
            generated_at=datetime.now().strftime("%Y-%m-%d"),
        )


# ═══════════════════════════════════════════════════════════
# 5. Pipeline
# ═══════════════════════════════════════════════════════════
class ArticleGenerator:
    """端到端生成管道"""

    def __init__(self):
        self.loader = DataLoader()
        self.router = ClusterRouter()
        self.seo = SEOOptimizer()
        self.builder = PromptBuilder()

    def generate_one(self, module_file: str, pattern_id: str) -> Path:
        """生成单篇文章，返回输出路径"""
        # Load
        module_data = self.loader.load_module(module_file)
        pattern = self.loader.get_pattern(module_data, pattern_id)
        if not pattern:
            raise ValueError(f"Pattern {pattern_id} not found in {module_file}")

        # Route
        cluster = self.router.route(module_data["module_id"])

        # SEO
        title = self.seo.generate_title(pattern)
        slug = self.seo.generate_slug(cluster["slug_prefix"], pattern)
        meta = self.seo.generate_meta(pattern)

        if not self.seo.validate_title(title):
            print(f"⚠ Title exceeds {self.seo.MAX_TITLE_LEN} chars: {title}")

        seo_data = {"title": title, "slug": slug, "meta_description": meta}

        # Render
        md_content = self.builder.render(
            module_data=module_data,
            pattern=pattern,
            cluster=cluster,
            seo=seo_data,
        )

        # Write
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        # slug → filename: /brooks-methodology/h2-bull-flag-guide → h2-bull-flag-guide.md
        filename = slug.rstrip("/").split("/")[-1] + ".md"
        out_path = OUTPUT_DIR / filename
        out_path.write_text(md_content, encoding="utf-8")
        print(f"✓ Generated: {out_path.relative_to(PROJECT_ROOT)}")
        return out_path

    def generate_all(self) -> list[Path]:
        """遍历所有模块的所有 pattern，批量生成"""
        results = []
        for module_data in self.loader.load_all_modules():
            module_id = module_data["module_id"]
            filename = f"{module_id}.json"
            for pattern in module_data.get("patterns", []):
                try:
                    path = self.generate_one(filename, pattern["pattern_id"])
                    results.append(path)
                except Exception as e:
                    print(f"✗ {module_id}/{pattern['pattern_id']}: {e}")
        return results


# ═══════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Brooks Encyclopedia → Article Generator")
    parser.add_argument("--module", "-m", help="Module JSON filename (e.g. M7_HIGH2.json)")
    parser.add_argument("--pattern", "-p", help="Pattern ID (e.g. H2_BULL_FLAG)")
    parser.add_argument("--all", action="store_true", help="Generate all patterns from all modules")
    args = parser.parse_args()

    gen = ArticleGenerator()

    if args.all:
        paths = gen.generate_all()
        print(f"\n=== Generated {len(paths)} articles ===")
    elif args.module and args.pattern:
        gen.generate_one(args.module, args.pattern)
    else:
        # Default: 端到端测试 M7_HIGH2 → H2_BULL_FLAG
        print("=== Default: M7_HIGH2 → H2_BULL_FLAG ===")
        gen.generate_one("M7_HIGH2.json", "H2_BULL_FLAG")
