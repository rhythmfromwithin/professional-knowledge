"""
将 inbox/*.md 中尚未发送到 Slack 的文章发送到 #inbox channel。
每篇文章发一条带三个按钮的 Block Kit 消息。
发送后将 slack_ts 写回 frontmatter，用于后续 update_frontmatter.py 定位文件。

所需环境变量:
  SLACK_BOT_TOKEN          - Bot User OAuth Token
  SLACK_INBOX_CHANNEL_ID   - #inbox channel 的 ID
"""
import os
import glob
import yaml
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


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


def build_blocks(title: str, link: str, source: str, priority: str) -> list:
    priority_emoji = {"high": "H", "medium": "M", "low": "L"}.get(priority, "?")
    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*{title}*\n{link}\nSource: {source}  |  Priority: [{priority_emoji}] {priority}",
            },
        },
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "High"},
                    "style": "danger",
                    "action_id": "interest_high",
                    "value": "high",
                },
                {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Medium"},
                    "action_id": "interest_medium",
                    "value": "medium",
                },
                {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Low"},
                    "style": "primary",
                    "action_id": "interest_low",
                    "value": "low",
                },
            ],
        },
    ]


def send_to_slack() -> None:
    token = os.environ["SLACK_BOT_TOKEN"]
    channel_id = os.environ["SLACK_INBOX_CHANNEL_ID"]
    client = WebClient(token=token)

    files = sorted(glob.glob("inbox/*.md"))
    sent = 0
    skipped = 0

    for path in files:
        fm, body = parse_frontmatter(path)
        if fm.get("slack_ts"):
            skipped += 1
            continue

        title = fm.get("title", os.path.basename(path))
        link = fm.get("link", "")
        source = fm.get("source", "Unknown")
        priority = fm.get("priority", "medium")

        try:
            resp = client.chat_postMessage(
                channel=channel_id,
                text=f"{title} - {link}",
                blocks=build_blocks(title, link, source, priority),
            )
            fm["slack_ts"] = resp["ts"]
            write_frontmatter(path, fm, body)
            sent += 1
            print(f"Sent: {title}")
        except SlackApiError as e:
            print(f"Error sending '{title}': {e.response['error']}")

    print(f"Done. Sent {sent}, skipped {skipped} (already sent).")


if __name__ == "__main__":
    send_to_slack()
