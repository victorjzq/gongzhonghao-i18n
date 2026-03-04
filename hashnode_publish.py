#!/usr/bin/env python3
"""批量发布英文文章到 Hashnode — 后台运行版"""

import glob
import json
import os
import sys
import time

# 强制无缓冲输出
sys.stdout.reconfigure(line_buffering=True)
sys.stderr.reconfigure(line_buffering=True)

import requests

# ---------------------------------------------------------------------------
# 环境变量
# ---------------------------------------------------------------------------
def _load_env():
    env_file = os.path.expanduser("~/.openclaw/wecom.env")
    if os.path.exists(env_file):
        with open(env_file) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                line = line.replace("export ", "", 1)
                if "=" not in line:
                    continue
                k, v = line.split("=", 1)
                os.environ[k.strip()] = v.strip().strip('"').strip("'")

_load_env()

HASHNODE_TOKEN = os.environ.get("HASHNODE_TOKEN", "")
PUBLICATION_ID = "69a46794a7428b958dd45a3c"
GQL_URL = "https://gql.hashnode.com"
HEADERS = {"Authorization": HASHNODE_TOKEN, "Content-Type": "application/json"}

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
PUBLISHED_FILE = os.path.join(PROJECT_DIR, "hashnode_published.json")
INTERVAL = 5  # 秒
NOTIFY_EVERY = 10  # 每 N 篇通知一次

# ---------------------------------------------------------------------------
# 企业微信通知
# ---------------------------------------------------------------------------
def notify(msg: str):
    try:
        sys.path.insert(0, os.path.expanduser("~/Claude-Global/Zoe"))
        from wecom import wecom_notify
        wecom_notify(msg)
    except Exception as e:
        print(f"[通知失败] {e}")


# ---------------------------------------------------------------------------
# 已发布记录
# ---------------------------------------------------------------------------
def load_published() -> dict:
    if os.path.exists(PUBLISHED_FILE):
        with open(PUBLISHED_FILE) as f:
            return json.load(f)
    return {}


def save_published(data: dict):
    with open(PUBLISHED_FILE, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# ---------------------------------------------------------------------------
# 发布单篇
# ---------------------------------------------------------------------------
def publish_one(filepath: str, title: str, body: str) -> dict | None:
    mutation = """
    mutation PublishPost($input: PublishPostInput!) {
      publishPost(input: $input) {
        post { id url title }
      }
    }
    """
    # 从目录名提取 tag
    rel = os.path.relpath(filepath, os.path.join(PROJECT_DIR, "translated/en"))
    category = rel.split(os.sep)[0] if os.sep in rel else "price-action"

    variables = {
        "input": {
            "title": title,
            "contentMarkdown": body,
            "publicationId": PUBLICATION_ID,
            "tags": [],
        }
    }

    try:
        r = requests.post(
            GQL_URL,
            json={"query": mutation, "variables": variables},
            headers=HEADERS,
            timeout=30,
        )
        data = r.json()
        if "errors" in data:
            return {"error": data["errors"][0].get("message", str(data["errors"]))}
        post = data["data"]["publishPost"]["post"]
        return {"id": post["id"], "url": post["url"], "title": post["title"]}
    except Exception as e:
        return {"error": str(e)}


# ---------------------------------------------------------------------------
# 主流程
# ---------------------------------------------------------------------------
def main():
    if not HASHNODE_TOKEN:
        print("❌ HASHNODE_TOKEN 未设置")
        return

    # 扫描文章
    files = sorted(glob.glob(
        os.path.join(PROJECT_DIR, "translated/en/**/*.md"),
        recursive=True,
    ))
    print(f"找到 {len(files)} 篇英文文章")

    published = load_published()
    print(f"已发布 {len(published)} 篇，跳过")

    ok_count = 0
    fail_count = 0
    skip_count = 0
    total = len(files)

    for i, fp in enumerate(files, 1):
        rel_path = os.path.relpath(fp, PROJECT_DIR)

        # 跳过已发布
        if rel_path in published:
            skip_count += 1
            continue

        # 读取文章
        with open(fp) as f:
            content = f.read().strip()
        if not content:
            skip_count += 1
            continue

        lines = content.split("\n")
        title = lines[0].lstrip("#").strip()
        body = "\n".join(lines[1:]).strip()

        if not title or not body:
            skip_count += 1
            continue

        # 发布
        result = publish_one(fp, title, body)

        if result and "error" not in result:
            ok_count += 1
            published[rel_path] = {
                "id": result["id"],
                "url": result["url"],
                "title": result["title"],
                "published_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            }
            save_published(published)
            print(f"[{i}/{total}] ✅ {title[:50]}")
        else:
            fail_count += 1
            err = result.get("error", "unknown") if result else "no response"
            published[rel_path] = {"error": err, "failed_at": time.strftime("%Y-%m-%d %H:%M:%S")}
            save_published(published)
            print(f"[{i}/{total}] ❌ {title[:50]} | {err[:80]}")

        # 每 N 篇通知
        done = ok_count + fail_count
        if done > 0 and done % NOTIFY_EVERY == 0:
            notify(
                f"📊 Hashnode 发布进度\n"
                f"✅ 成功: {ok_count} | ❌ 失败: {fail_count}\n"
                f"进度: {i}/{total} ({i*100//total}%)"
            )

        time.sleep(INTERVAL)

    # 最终汇报
    summary = (
        f"🎉 Hashnode 批量发布完成\n"
        f"总计: {total} 篇\n"
        f"✅ 成功: {ok_count}\n"
        f"❌ 失败: {fail_count}\n"
        f"⏭️ 跳过: {skip_count}\n"
        f"🔗 https://victorjia.hashnode.dev"
    )
    print(summary)
    notify(summary)


if __name__ == "__main__":
    main()
