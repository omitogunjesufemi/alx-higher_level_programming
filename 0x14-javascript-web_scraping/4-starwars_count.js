#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

const characters = [];
request(url, (error, response, body) => {
  if (error) return;
  const allFilms = JSON.parse(body);

  if (allFilms.results.length === 0) return;
  for (const film of allFilms.results) {
    if (film.characters.length === 0) return;
    for (const character of film.characters) {
      if (character === 'https://swapi-api.alx-tools.com/api/people/18/') {
        characters.push(character);
      }
    }
  }
  console.log(characters.length);
});
