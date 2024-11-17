from bs4 import BeautifulSoup as bs
import urllib.request
from datetime import datetime
import re

from github_issue import make_github_issue
from config import SEARCH_URLS, KEYWORDS

def get_paper_id(result):
    paper_number = result.find("p", {"class": "list-title"}).text
    # Extract arXiv number using regex
    match = re.search(r'arXiv:\d+\.\d+(v\d+)?', paper_number)
    if match:
        arxiv_id_text = match.group(0)
        return arxiv_id_text.split(":")[-1].strip()

def load_past_papers():
    with open("past_papers.txt", "r") as file:
        content = file.read()
        return content.split(";")

def add_to_past_papers(papers):
    with open("past_papers.txt", "a") as file:
        file.write(";")
        file.write(";".join(papers))

def main():
    past_papers = load_past_papers()
    for search_url in SEARCH_URLS:
        page = urllib.request.urlopen(search_url)
        soup = bs(page, "html.parser")
        content = soup.body.find("div", {"class": "content"})

        issue_title = f"Notifications for {datetime.now().strftime('%Y-%m-%d')}"
        arxiv_base = "https://arxiv.org/abs/"
        result_list = content.find_all("li", {"class": "arxiv-result"})
        papers = []

        for result in result_list:
            paper = {}
            paper_number = get_paper_id(result)

            if paper_number in past_papers:
                continue
            
            paper["number"] = paper_number
            paper["url"] = arxiv_base + paper_number
            paper["pdf"] = arxiv_base.replace("abs", "pdf") + paper_number
            paper["title"] = result.find("p", {"class": "title is-5 mathjax"}).text.strip()
            paper["authors"] = re.sub("\s+", " ", result.find("p", {"class": "authors"}).text.replace("Authors:", "").replace("\n", "").strip())
            paper["subjects"] = ", ".join([tag["data-tooltip"] + f" ({tag.text})" for tag in result.find("div", {"class": "tags"}).find_all("span")])
            paper["abstract"] = result.find("span", {"class": "abstract-full"}).text.replace("Abstract:", "").replace("△ Less", "").strip()
            papers.append(paper)

        full_report = ""
        
        for paper in papers:
            report = "### {}\n - **Authors:** {}\n - **Subjects:** {}\n - **Arxiv link:** {}\n - **Pdf link:** {}\n - **Abstract**\n {}" \
                .format(paper["title"], paper["authors"], paper["subjects"], paper["url"], paper["pdf"],
                        paper["abstract"])
            full_report = full_report + report + "\n\n"

        make_github_issue(title=issue_title, body=full_report, labels=KEYWORDS)
        add_to_past_papers([paper["number"] for paper in papers])

if __name__ == "__main__":
    main()
