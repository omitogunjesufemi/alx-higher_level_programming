#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status
using requests library
"""
import requests

res = requests.get("https://alx-intranet.hbtn.io/status")
body = res.text
print("Body response:")
print(f"\t- type: {type(body)}")
print(f"\t- content: {body}")
