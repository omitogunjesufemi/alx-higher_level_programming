#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url).on('error', (error) => {
  if (error) console.log(error);
}).on('response', (response) => {
  console.log('code:', response.statusCode);
});
