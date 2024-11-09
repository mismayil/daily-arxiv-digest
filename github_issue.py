import json
import requests
import os
from config import USERNAME, REPO_OWNER, REPO_NAME

def make_github_issue(title, body=None, assignee=USERNAME, closed=False, labels=[]):
    # Create an issue on github.com using the given parameters
    # Url to create issues via POST
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/import/issues"

    # Headers
    headers = {
        "Authorization": f"token {os.environ['ISSUE_TOKEN']}",
        "Accept": "application/vnd.github.golden-comet-preview+json"
    }

    # Create our issue
    data = {"issue": {"title": title,
                      "body": body,
                      "assignee": assignee,
                      "closed": closed,
                      "labels": labels}}

    payload = json.dumps(data)

    # Add the issue to our repository
    response = requests.request("POST", url, data=payload, headers=headers)
    if response.status_code == 202:
        print(f"Successfully created Issue [{title}]")
    else:
        print(f"Could not create Issue [{title}]")
        print("Response:", response.content)

if __name__ == "__main__":
    title = "Pretty title"
    body = "Beautiful body"
    assignee = USERNAME
    closed = False
    labels = [
        "imagenet", "image retrieval"
    ]

    make_github_issue(title, body, assignee, closed, labels)
