# 0x10. Python - Network #1
This project helped to understand the following:
- How to fetch internet resources with the Python package urllib
- How to decode urllib body response
- How to use the Python package requests #requestsiswaysimplerthanurllib
- How to make HTTP GET request
- How to make HTTP POST/PUT/etc. request
- How to fetch JSON resources
- How to manipulate data from an external service

The following tasks where in the project:
TASK | DESCRIPTION
--- | ---
`0-hbtn_status.py` | Script fetches https://alx-intranet.hbtn.io/status
`1-hbtn_header.py` | Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.
`2-post_email.py` | Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
`3-error_code.py` | Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8)
`4-hbtn_status.py` | Python script that fetches https://alx-intranet.hbtn.io/status using requests library
`5-hbtn_header` | Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header
`6-post_email.py` | Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response using requests
`7-error_code.py` | Python script that takes in a URL, sends a request to the URL and displays the body of the response. If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code
`8-json_api.py` | Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter
`10-my_github.py` | Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id
`100-github_commits.py` | Python Script that list 10 commits (from the most recent to oldest) of the repository by the user

