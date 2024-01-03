#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) return;

  const movie = JSON.parse(body);
  const characters = movie.characters;

  for (const character of characters) {
    request(character, (err, resp, bdy) => {
      if (err) return;
      const character = JSON.parse(bdy);
      console.log(character.name);
    });
  }
});
