#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const fileName = process.argv[3];

request.get(url).pipe(fs.createWriteStream(fileName));
