"""
创建 Slack channels（如不存在则新建），并打印各 channel ID。
运行一次后，将输出的 ID 配置为 GitHub Actions / Render 的环境变量。

所需 Bot Token Scopes:
  channels:manage  - 创建 public channel
  channels:read    - 列出已有 channel
"""
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

CHANNEL_NAMES = ["inbox", "dive-deep", "need-to-scan", "ignore"]


def get_existing_channels(client: WebClient) -> dict:
    existing = {}
    cursor = None
    while True:
        resp = client.conversations_list(
            types="public_channel",
            cursor=cursor,
            limit=200,
        )
        for ch in resp["channels"]:
            existing[ch["name"]] = ch["id"]
        cursor = resp.get("response_metadata", {}).get("next_cursor")
        if not cursor:
            break
    return existing


def setup_channels() -> None:
    token = os.environ["SLACK_BOT_TOKEN"]
    client = WebClient(token=token)

    existing = get_existing_channels(client)

    print("Channel IDs (paste these into your environment variables):\n")
    for name in CHANNEL_NAMES:
        if name in existing:
            ch_id = existing[name]
            print(f"  #{name} already exists -> {ch_id}")
        else:
            try:
                resp = client.conversations_create(name=name, is_private=False)
                ch_id = resp["channel"]["id"]
                print(f"  #{name} created       -> {ch_id}")
            except SlackApiError as e:
                print(f"  #{name} ERROR: {e.response['error']}")
                continue

        env_key = "SLACK_" + name.upper().replace("-", "_") + "_CHANNEL_ID"
        print(f"    export {env_key}={ch_id}")

    print("\nDone.")


if __name__ == "__main__":
    setup_channels()
