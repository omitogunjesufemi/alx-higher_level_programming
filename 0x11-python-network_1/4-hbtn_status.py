#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status
using requests library
"""
import requests

res = requests.get("https://alx-intranet.hbtn.io/status")
body = res.text
print(f"""Body response:
    - type: {type(body)}
    - content: {body}""")
