#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        q = ""
        print("No result")
    else:
        q = sys.argv[1]
        url = "http://0.0.0.0:5000/search_user"
        res = requests.post(url, data={'q': q})
        output = eval(res.content)
        if type(output) is not dict:
            print("Not a valid JSON")
        if len(output) == 0:
            print("No result")
        else:
            print("[{}] {}".format(output['id'],
                                   output['name']))
