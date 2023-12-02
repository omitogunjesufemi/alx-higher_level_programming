#!/usr/bin/python3
"""Python Script that list 10 commits (from the most recent to oldest) of
the repository by the user
"""
import sys
import requests


if __name__ == "__main__":
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    headers = {"Accept": "application/vnd.github+json",
               "X-GitHub-Api-Version": "2022-11-28"}
    res = requests.get(url, headers=headers)
    body = res.json()
    commits = body[:10]
    for commit in commits:
        print("{}: {}".format(commit.get('sha'),
                              commit.get('commit')
                              .get('author').get('name')))
