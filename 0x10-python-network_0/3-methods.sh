#!/bin/bash
# Script takes URL displays all HTTP methods the server will accept
curl -sIX OPTIONS "$1" | grep "Allow" | cut -c 8-
