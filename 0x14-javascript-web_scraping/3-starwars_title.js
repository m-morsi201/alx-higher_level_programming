#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode number matches a given integer.
const request = require('request');
const Url = 'https://swapi-api.hbtn.io/api/films';
//  The first argument is the movie ID
const MovieId = process.argv[2];

request(`${Url}/${MovieId}/`, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const json = JSON.parse(body);
  console.log(json.title);
});
