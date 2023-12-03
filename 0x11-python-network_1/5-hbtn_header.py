#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in the response header
"""
import requests
import sys


if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    try:
        header = res.headers["X-Request-Id"]
        print(header)
    except:
        return None
