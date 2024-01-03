#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

request(url, (error, response, body) => {
  if (error) console.log(error);
  const jsonOut = JSON.parse(body);
  console.log(jsonOut.title);
});
