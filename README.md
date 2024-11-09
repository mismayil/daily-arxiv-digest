# daily-arxiv-notifications

This repo is a modified fork of [get-daily-arxiv-noti](https://github.com/kobiso/get-daily-arxiv-noti).

You can get daily arxiv notification with pre-defined keywords as [here](https://github.com/mismayil/daily-arxiv-notifications/issues).

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
Create a repository to get notification in your github. This repo uses Github Actions to post a new issue in the repo. So, it needs access to create issues in the repo. To do this, create a new fine-grained token in [here](https://github.com/settings/tokens?type=beta) and then add this new token as a secret named `ISSUE_TOKEN` in your [repo settings](https://github.com/mismayil/daily-arxiv-notifications/settings/secrets/actions).

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
```

#### 3. Adjust schedule
This repo uses Github Actions to run a cron job every day. You can modify the schedule in [github-actions.yml](.github/workflows/github-actions.yml) by adjusting `cron` parameters. See [crontab](https://crontab.guru/) for more information on cron job parameters.