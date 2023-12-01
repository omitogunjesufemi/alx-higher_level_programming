#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    url = f"https://api.github.com/users/{sys.argv[1]}"
    token = sys.argv[2]
    headers = {"Accept": "application/vnd.github+json",
               "X-GitHub-Api-Version": "2022-11-28",
               "Authorization": f"Bearer {token}"}
    res = requests.get(url, headers=headers)
    body = eval(res.content.decode()
                .replace('false', 'False').replace('null', 'None'))
    print(body.get('id'))
