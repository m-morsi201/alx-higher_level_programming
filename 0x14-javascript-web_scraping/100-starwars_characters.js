#!/usr/bin/node
// script that prints all characters of a Star Wars movie
const request = require('request');
// The first argument is the Movie ID
const Id = process.argv[2];
// The url of  Star wars API.
const Url = 'https://swapi-api.hbtn.io/api/films/';

request.get(Url + Id, function (error, resp, body) {
  if (error) {
    console.log(error);
  }
  const Json = JSON.parse(body);
  const temp = Json.characters;
  for (const i of temp) {
    request.get(i, function (error, resp, body1) {
      if (error) {
        console.log(error);
      }
      const Data = JSON.parse(body1);
      console.log(Data.name);
    });
  }
});
