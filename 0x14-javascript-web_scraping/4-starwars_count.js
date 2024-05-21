#!/usr/bin/node
// Script that prints the number of movies where the character “Wedge Antilles” is present.
const request = require('request');
// The first argument is the API URL.
const Url = process.argv[2];

request(Url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (body) {
    const Json = JSON.parse(body);
    const CharFilm = Json.results.filter(
      x => x.characters.find(y => y.match(/\/people\/18\/?$/))
    );
    console.log(CharFilm.length);
  }
});
