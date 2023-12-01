#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status
"""
from urllib.request import urlopen

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urlopen(url) as response:
        body = response.read()
        decode = body.decode('utf8')
    print(f"""Body response:
    - type: {type(body)}
    - content: {body}
    - utf8 content: {decode}""")
