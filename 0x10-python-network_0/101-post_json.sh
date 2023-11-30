#!/bin/bash
# script that sends a JSON POST request to a URL and displays body of response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
