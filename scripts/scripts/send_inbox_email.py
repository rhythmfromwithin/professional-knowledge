import os
import glob
import smtplib
from email.message import EmailMessage

import yaml


def parse_frontmatter(path: str) -> dict:
    """
    解析 markdown 文件顶部的 YAML frontmatter。
    """
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


def build_inbox_summary(inbox_dir: str = "inbox") -> str:
    """
    汇总 inbox 中所有条目的关键信息，用于邮件正文。
    """
    files = sorted(glob.glob(os.path.join(inbox_dir, "*.md")))
    parts: list[str] = []

    for path in files:
        meta = parse_frontmatter(path)
        title = meta.get("title", os.path.basename(path))
        source = meta.get("source", "Unknown")
        link = meta.get("link", "")
        priority = meta.get("priority", "")
        status = meta.get("status", "")
        interest = meta.get("interest", "")
        next_step = meta.get("next_step", "")

        section_lines = [
            f"Title   : {title}",
            f"Source  : {source}",
            f"Link    : {link}",
            f"Priority: {priority}",
            f"Status  : {status}",
            f"Interest: {interest}",  # High / Medium / Low
            f"NextStep: {next_step}",  # deep_read / skim / ignore
            f"File    : {os.path.basename(path)}",
        ]
        parts.append("\n".join(section_lines))

    header = "AI related blogs / research / VC News inbox overview\n"
    header += "（在 markdown 文件里编辑 Interest 和 NextStep 字段来标记个人偏好）\n\n"

    return header + ("\n\n" + ("-" * 40) + "\n\n").join(parts)


def send_email(body: str) -> None:
    """
    通过 Gmail SMTP 发送邮件。
    需要环境变量:
      - GMAIL_USERNAME: 你的 Gmail 地址
      - GMAIL_APP_PASSWORD: Gmail 应用专用密码
      - GMAIL_TO: 可选，收件人地址（默认等于 GMAIL_USERNAME）
    """
    username = os.environ.get("GMAIL_USERNAME")
    password = os.environ.get("GMAIL_APP_PASSWORD")
    to_addr = os.environ.get("GMAIL_TO", username)

    if not username or not password:
        raise RuntimeError(
            "缺少 GMAIL_USERNAME 或 GMAIL_APP_PASSWORD 环境变量，"
            "请先在系统或 shell 中配置后再运行。"
        )

    if not to_addr:
        raise RuntimeError("无法确定收件人邮箱，请设置 GMAIL_TO 或 GMAIL_USERNAME。")

    msg = EmailMessage()
    msg["Subject"] = "aI related blogs_researchs_VCNews"
    msg["From"] = username
    msg["To"] = to_addr
    msg.set_content(body)

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(username, password)
        smtp.send_message(msg)


if __name__ == "__main__":
    summary = build_inbox_summary()
    send_email(summary)

