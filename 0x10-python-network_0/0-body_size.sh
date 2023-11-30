#!/bin/bash
# A script that displays size of the body of the response

curl -sI "$1" | grep "Content-Length" | cut -c 17-
