from datetime import datetime, timedelta

# Authentication for user filing issue (must have read/write access to repository to add issue to)
USERNAME = "mismayil"

# The repository to add this issue to
REPO_OWNER = "mismayil"
REPO_NAME = "daily-arxiv-digest"

num_days = 1

# if it is monday, get the papers from friday, saturday and sunday
if datetime.today().weekday() == 0:
    num_days = 3

from_date = (datetime.now() - timedelta(days=num_days)).strftime("%Y-%m-%d")
# Set submission url(s) of subject
SEARCH_URLS = [f"https://arxiv.org/search/advanced?advanced=&terms-0-operator=AND&terms-0-term=creative&terms-0-field=all&terms-1-operator=OR&terms-1-term=creativity&terms-1-field=all&classification-computer_science=y&classification-physics_archives=all&classification-include_cross_list=include&date-year=&date-filter_by=date_range&date-from_date={from_date}&date-to_date=&date-date_type=submitted_date&abstracts=show&size=200&order=-announced_date_first"]

KEYWORDS = ["creativity", "creative"]

SLACK_CHANNEL_ID = "C082FEKK788"