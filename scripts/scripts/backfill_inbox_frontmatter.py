"""
给 inbox 根目录下没有 interest / next_step 的 .md 文章补全 frontmatter 字段：
  interest: medium
  next_step: skim
只处理 inbox/*.md，不处理 inbox/deep_reading/、inbox/skim_reading/ 等子目录。
"""
import os
import glob


def backfill_file(path: str) -> bool:
    """若缺少 interest 或 next_step 则补全并写回，返回是否修改过。"""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    parts = content.split("---", 2)
    if len(parts) != 3:
        return False
    before, frontmatter, body = parts
    frontmatter = frontmatter.strip()
    modified = False

    if "interest:" not in frontmatter:
        frontmatter = frontmatter + "\ninterest: medium"
        modified = True
    if "next_step:" not in frontmatter:
        frontmatter = frontmatter + "\nnext_step: skim"
        modified = True

    if not modified:
        return False

    new_content = "---" + "\n" + frontmatter + "\n---" + body
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True


def main():
    inbox_root = "inbox"
    pattern = os.path.join(inbox_root, "*.md")
    files = sorted(glob.glob(pattern))
    updated = 0
    for path in files:
        if backfill_file(path):
            updated += 1
            print(path)
    print(f"Done. Updated {updated} of {len(files)} files.")


if __name__ == "__main__":
    main()
