"""
根据 SLACK_TS 和 INTEREST 环境变量，在 inbox/*.md 中找到对应文章，
更新 frontmatter（interest / next_step），并将文件移动到对应子目录。

子目录映射:
  high   -> inbox/dive-deep/
  medium -> inbox/need-to-scan/
  low    -> inbox/ignore/

由 GitHub Actions update-inbox.yml 调用。
"""
import os
import glob
import shutil
import yaml

DEST_MAP = {
    "high": os.path.join("inbox", "dive-deep"),
    "medium": os.path.join("inbox", "need-to-scan"),
    "low": os.path.join("inbox", "ignore"),
}

NEXT_STEP_MAP = {
    "high": "deep_read",
    "medium": "skim",
    "low": "ignore",
}


def parse_frontmatter(path: str):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    parts = content.split("---", 2)
    if len(parts) != 3:
        return {}, content
    _, fm_str, body = parts
    try:
        fm = yaml.safe_load(fm_str) or {}
    except Exception:
        fm = {}
    return fm, body


def write_frontmatter(path: str, fm: dict, body: str) -> None:
    fm_str = yaml.dump(fm, allow_unicode=True, default_flow_style=False).strip()
    new_content = f"---\n{fm_str}\n---{body}"
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)


def main() -> None:
    slack_ts = os.environ.get("SLACK_TS", "").strip()
    interest = os.environ.get("INTEREST", "").strip().lower()

    if not slack_ts:
        raise SystemExit("ERROR: SLACK_TS environment variable is required.")
    if interest not in DEST_MAP:
        raise SystemExit(f"ERROR: INTEREST must be high/medium/low, got: {interest!r}")

    dest_dir = DEST_MAP[interest]
    os.makedirs(dest_dir, exist_ok=True)

    # Search only inbox root, not subdirectories
    found = None
    for path in glob.glob(os.path.join("inbox", "*.md")):
        fm, body = parse_frontmatter(path)
        if str(fm.get("slack_ts", "")).strip() == slack_ts:
            found = (path, fm, body)
            break

    if not found:
        raise SystemExit(f"ERROR: No inbox/*.md file with slack_ts={slack_ts!r}")

    path, fm, body = found
    fm["interest"] = interest
    fm["next_step"] = NEXT_STEP_MAP[interest]

    dest_path = os.path.join(dest_dir, os.path.basename(path))
    write_frontmatter(path, fm, body)
    shutil.move(path, dest_path)
    print(f"Moved: {path} -> {dest_path}")


if __name__ == "__main__":
    main()
