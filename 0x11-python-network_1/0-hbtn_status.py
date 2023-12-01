#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status
"""
from urllib.request import urlopen

url = "https://alx-intranet.hbtn.io/status"
with urlopen(url) as response:
    body = response.read()
    decode = body.decode('utf8')
    print(f"""Body response:
    \t- type: {type(body)}
    \t- content: {body}
    \t- utf8 content: {decode}""")
