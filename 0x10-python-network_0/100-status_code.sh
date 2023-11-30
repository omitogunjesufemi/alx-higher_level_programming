#!/bin/bash
# Script sends a request to a URL and display only status code of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
