#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays
the body of the response. If the HTTP status code is greater than or equal to
400, print: Error code: followed by the value of the HTTP status code
"""
import sys
import requests


if __name__ == "__main__":
    try:
        res = requests.get(sys.argv[1])
        res.raise_for_status()
        print(res.text)
    except requests.HTTPError as er:
        print(f"Error code: {er.response.status_code}")
