"""
Slack Bolt app - deployed to Render.
Handles button interactions from #inbox messages:
  - Posts article to the target channel (dive-deep / need-to-scan / ignore)
  - Updates the original #inbox message to show it has been labeled
  - Triggers GitHub Actions to update the .md frontmatter and move the file

Required environment variables (set in Render dashboard):
  SLACK_BOT_TOKEN              - Bot User OAuth Token (xoxb-...)
  SLACK_SIGNING_SECRET         - Slack App Signing Secret
  SLACK_DIVE_DEEP_CHANNEL_ID   - #dive-deep channel ID
  SLACK_NEED_SCAN_CHANNEL_ID   - #need-to-scan channel ID
  SLACK_IGNORE_CHANNEL_ID      - #ignore channel ID
  GH_PAT                       - GitHub Personal Access Token (repo + workflow scope)
  GH_REPO                      - e.g. "your-github-username/professional-knowledge"
"""
import os
import requests
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
from flask import Flask, request

app = App(
    token=os.environ["SLACK_BOT_TOKEN"],
    signing_secret=os.environ["SLACK_SIGNING_SECRET"],
)

CHANNEL_MAP = {
    "high": os.environ.get("SLACK_DIVE_DEEP_CHANNEL_ID", ""),
    "medium": os.environ.get("SLACK_NEED_SCAN_CHANNEL_ID", ""),
    "low": os.environ.get("SLACK_IGNORE_CHANNEL_ID", ""),
}

LABEL_MAP = {
    "high": ("High", "#dive-deep"),
    "medium": ("Medium", "#need-to-scan"),
    "low": ("Low", "#ignore"),
}


def trigger_github_actions(slack_ts: str, interest: str) -> None:
    gh_token = os.environ.get("GH_PAT", "")
    gh_repo = os.environ.get("GH_REPO", "")
    if not gh_token or not gh_repo:
        print("GH_PAT or GH_REPO not configured, skipping git sync.")
        return

    url = f"https://api.github.com/repos/{gh_repo}/actions/workflows/update-inbox.yml/dispatches"
    resp = requests.post(
        url,
        json={
            "ref": "main",
            "inputs": {"slack_ts": slack_ts, "interest": interest},
        },
        headers={
            "Authorization": f"Bearer {gh_token}",
            "Accept": "application/vnd.github+json",
        },
        timeout=10,
    )
    if resp.status_code == 204:
        print(f"GitHub Actions triggered: slack_ts={slack_ts}, interest={interest}")
    else:
        print(f"GitHub Actions trigger failed: {resp.status_code} {resp.text}")


def handle_interest(interest: str, body: dict, client, ack) -> None:
    ack()

    message = body["message"]
    channel_id = body["channel"]["id"]
    message_ts = message["ts"]

    # Pull article text from original message blocks
    article_text = ""
    for block in message.get("blocks", []):
        if block.get("type") == "section":
            article_text = block.get("text", {}).get("text", "")
            break

    label, target_channel_name = LABEL_MAP[interest]
    target_channel_id = CHANNEL_MAP[interest]

    # 1. Post to target channel
    print(f"Attempting to post to channel: {target_channel_id} ({target_channel_name})")
    print(f"article_text preview: {article_text[:80]!r}")
    if target_channel_id:
        try:
            resp = client.chat_postMessage(
                channel=target_channel_id,
                text=article_text,
                blocks=[
                    {
                        "type": "section",
                        "text": {"type": "mrkdwn", "text": article_text},
                    },
                    {
                        "type": "context",
                        "elements": [
                            {"type": "mrkdwn", "text": f"Interest: *{label}*"}
                        ],
                    },
                ],
            )
            print(f"chat_postMessage ok={resp.get('ok')}, ts={resp.get('ts')}, channel={resp.get('channel')}")
        except Exception as e:
            print(f"Error posting to {target_channel_name}: {e}")
    else:
        print(f"Skipped: target_channel_id is empty for interest={interest}")

    # 2. Update original #inbox message: remove buttons, show label
    try:
        client.chat_update(
            channel=channel_id,
            ts=message_ts,
            text=article_text,
            blocks=[
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": article_text},
                },
                {
                    "type": "context",
                    "elements": [
                        {
                            "type": "mrkdwn",
                            "text": f"Labeled: *{label}* -> {target_channel_name}",
                        }
                    ],
                },
            ],
        )
    except Exception as e:
        print(f"Error updating original message: {e}")

    # 3. Trigger GitHub Actions to sync .md file
    trigger_github_actions(message_ts, interest)


@app.action("interest_high")
def on_high(body, client, ack):
    handle_interest("high", body, client, ack)


@app.action("interest_medium")
def on_medium(body, client, ack):
    handle_interest("medium", body, client, ack)


@app.action("interest_low")
def on_low(body, client, ack):
    handle_interest("low", body, client, ack)


# Flask wrapper
flask_app = Flask(__name__)
handler = SlackRequestHandler(app)


@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)


@flask_app.route("/health", methods=["GET"])
def health():
    return "ok", 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    flask_app.run(host="0.0.0.0", port=port)
