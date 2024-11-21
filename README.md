# daily-arxiv-digest

This repo is a modified fork of [get-daily-arxiv-noti](https://github.com/kobiso/get-daily-arxiv-noti).

You can get daily arxiv digests with pre-defined keywords as [here](https://github.com/mismayil/daily-arxiv-digest/issues).

Arxiv.org announces new submissions every day on fixed time as informed [here](https://arxiv.org/help/submit).

This repository makes it easy to filter papers and follow-up new papers which are in your interests by creating an issue in a github repository.


## Prerequisites
- Python3.10

Install requirements with below command.

```bash
$ pip install --upgrade pip
$ pip install -r requirements.txt
```

## Usage

#### 1. Create a Repo
Create a repository to get your daily arxiv digest in your github. This repo uses Github Actions to post a new issue in the repo and optionally send a message to a Slack channel. So, it needs access to create issues in the repo and send messages to Slack. To do this, create a new fine-grained token in [here](https://github.com/settings/tokens?type=beta) and then add this new token as a secret named `ISSUE_TOKEN` in your [repo settings](https://github.com/mismayil/daily-arxiv-digest/settings/secrets/actions). To send a message to Slack channel, [create an app](https://api.slack.com/quickstart#creating) in your Slack workspace, specify the channel ID in the `config.py` and also add the OAuth token generated when you create the app as a secret named `SLACK_BOT_TOKEN` in your [repo settings](https://github.com/mismayil/daily-arxiv-digest/settings/secrets/actions).

#### 2. Set Config
Revise `config.py` as your perferences.

```python
# Authentication for user filing issue (must have read/write access to repository to add issue to)
USERNAME = 'changeme'

# The repository to add this issue to
REPO_OWNER = 'changeme'
REPO_NAME = 'changeme'

# Set new submission url of subject.
# Create a search url from https://arxiv.org/search/advanced. By default, search starts from the previous day.
SEARCH_URLS = []

# Keywords to search. These keywords are only used to create labels for the github issue. Use the advanced search https://arxiv.org/search/advanced to set your keywords.
KEYWORD_LIST = ["changeme"]

# Slack channel id to send a notification message about the github issue. Set to None if you dont to set it up
SLACK_CHANNEL_ID = "changeme"
```

#### 3. Adjust schedule
This repo uses Github Actions to run a cron job every day. You can modify the schedule in [github-actions.yml](.github/workflows/github-actions.yml) by adjusting `cron` parameters. See [crontab](https://crontab.guru/) for more information on cron job parameters.