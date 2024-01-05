#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

const wedgeAntillesId = 18;

request(apiUrl, (error, response, body) => {
  if (error) console.error('Error:', error);

  const filmsData = JSON.parse(body);

  const filmsWithWedgeAntilles = filmsData.results.filter((film) =>
    film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`)
  );

  console.log(filmsWithWedgeAntilles.length);
});
