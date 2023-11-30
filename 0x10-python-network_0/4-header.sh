#!/bin/bash
# Script that take URL with header variable, display body of response
curl -sH "X-School-User-Id: 98" "$1"
