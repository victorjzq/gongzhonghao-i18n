#!/usr/bin/env python3
"""
一键发布到所有平台
用法: python publish_all.py --lang en --status draft
"""

import os
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
SCRIPTS_DIR = Path(__file__).parent


def check_env():
    """检查哪些平台的凭证已配置"""
    env_file = BASE_DIR / ".env"
    configured = {}

    if not env_file.exists():
        print("WARNING: .env file not found. Copy .env.example to .env and fill in credentials.")
        return configured

    env_content = env_file.read_text()
    checks = {
        "medium": ("MEDIUM_TOKEN", "publish_medium.py"),
        "substack": ("SUBSTACK_SID", "publish_substack.py"),
        "devto": ("DEVTO_API_KEY", "publish_devto.py"),
    }

    for platform, (env_var, script) in checks.items():
        for line in env_content.splitlines():
            if line.startswith(f"{env_var}="):
                val = line.split("=", 1)[1].strip().strip('"').strip("'")
                if val and not val.startswith("your_"):
                    configured[platform] = script
                    break

    return configured


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Publish to all configured platforms")
    parser.add_argument("--lang", required=True, help="Language code")
    parser.add_argument("--status", default="draft", choices=["draft", "public"])
    parser.add_argument("--category", help="Only publish specific category")
    parser.add_argument("--limit", type=int, default=0, help="Max articles per platform")
    args = parser.parse_args()

    configured = check_env()

    if not configured:
        print("\n❌ No platforms configured!")
        print("\nTo get started:")
        print("  1. cp .env.example .env")
        print("  2. Fill in API tokens for at least one platform:")
        print("     - Medium: Settings → Security → Integration tokens")
        print("     - Substack: Browser DevTools → Cookies → substack.sid")
        print("     - Dev.to: https://dev.to/settings/extensions → Generate API Key")
        print("  3. Re-run this script")
        return

    print(f"Configured platforms: {', '.join(configured.keys())}")
    print(f"Language: {args.lang}, Status: {args.status}")
    print("=" * 50)

    for platform, script in configured.items():
        print(f"\n>>> Publishing to {platform}...")
        cmd = [sys.executable, str(SCRIPTS_DIR / script), "--lang", args.lang]

        if platform == "medium":
            cmd.extend(["--status", args.status])
        elif platform == "substack":
            # Substack needs subdomain — check env
            env_content = (BASE_DIR / ".env").read_text()
            subdomain = None
            for line in env_content.splitlines():
                if line.startswith("SUBSTACK_SUBDOMAIN="):
                    subdomain = line.split("=", 1)[1].strip().strip('"').strip("'")
            if subdomain:
                cmd.extend(["--subdomain", subdomain])
            else:
                print(f"  SKIP: SUBSTACK_SUBDOMAIN not set in .env")
                continue

        if args.category:
            cmd.extend(["--category", args.category])
        if args.limit:
            cmd.extend(["--limit", str(args.limit)])

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            print(result.stdout)
            if result.stderr:
                print(f"  STDERR: {result.stderr}")
        except Exception as e:
            print(f"  ERROR: {e}")

    print("\n" + "=" * 50)
    print("All platforms processed.")


if __name__ == "__main__":
    main()
