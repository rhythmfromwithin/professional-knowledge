"""
按 frontmatter 的 next_step 将 inbox 根目录下的文章移动到子目录：
  next_step: deep_read  -> inbox/deep_reading/
  next_step: skim       -> inbox/skim_reading/
  next_step: ignore 或未设置 -> 不移动
只处理 inbox/*.md，不处理子目录中已有文件。
"""
import os
import glob
import shutil
import yaml


def parse_frontmatter(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    if not lines or not lines[0].strip().startswith("---"):
        return {}
    yaml_lines = []
    for line in lines[1:]:
        if line.strip().startswith("---"):
            break
        yaml_lines.append(line)
    try:
        return yaml.safe_load("".join(yaml_lines)) or {}
    except Exception:
        return {}


def main():
    inbox_root = "inbox"
    deep_dir = os.path.join(inbox_root, "deep_reading")
    skim_dir = os.path.join(inbox_root, "skim_reading")
    os.makedirs(deep_dir, exist_ok=True)
    os.makedirs(skim_dir, exist_ok=True)

    files = sorted(glob.glob(os.path.join(inbox_root, "*.md")))
    moved_deep = 0
    moved_skim = 0
    for path in files:
        meta = parse_frontmatter(path)
        next_step = (meta.get("next_step") or "").strip().lower()
        if next_step == "deep_read":
            dest = deep_dir
            moved_deep += 1
        elif next_step == "skim":
            dest = skim_dir
            moved_skim += 1
        else:
            continue
        dest_path = os.path.join(dest, os.path.basename(path))
        shutil.move(path, dest_path)
        print(f"  {os.path.basename(path)} -> {dest}/")
    print(f"Done. Moved {moved_deep} to deep_reading, {moved_skim} to skim_reading.")


if __name__ == "__main__":
    main()
