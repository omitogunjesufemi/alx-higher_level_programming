#!/bin/bash
# Script that sends POST request to the passed URL, display body of response
curl -sX POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
