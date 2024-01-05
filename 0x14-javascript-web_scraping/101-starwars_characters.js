#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (err, resp, bdy) => {
  if (err) return;

  const movie = JSON.parse(bdy);
  const characters = movie.characters;

  const fetchCharacterData = (cUrl) => {
    request(cUrl, (cErr, cResp, cBody) => {
      if (cErr) {
        console.log(cErr);
      } else {
        const characterName = JSON.parse(cBody);
        console.log(characterName.name);

        const nextChar = characters.shift();
        if (nextChar) fetchCharacterData(nextChar);
      }
    });
  };

  const firstChar = characters.shift();
  if (firstChar) fetchCharacterData(firstChar);
});
