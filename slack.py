import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


def send_message(channel_id, text):
    client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))
    try:
        result = client.chat_postMessage(
            channel=channel_id,
            text=text
        )
        if result and result["ok"]:
            print(f"Message sent successfully to {channel_id}")
    except SlackApiError as e:
        print(f"Error: {e}")