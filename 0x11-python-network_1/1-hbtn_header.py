#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found in the header of
the response.
"""
from urllib.request import urlopen
import sys

if __name__ == "__main__":
    with urlopen(sys.argv[1]) as response:
        body = response
        print(body.headers["X-Request-Id"])
