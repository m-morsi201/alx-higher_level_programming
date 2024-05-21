#!/usr/bin/node
// script that prints all characters of a Star Wars movie
const request = require('request');
// The url of  Star wars API.
const Url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(Url, function (error, response, body) {
  if (!error) {
    const Chars = JSON.parse(body).characters;
    PrintChars(Chars, 0);
  }
});

function PrintChars (Chars, index) {
  request(Chars[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < Chars.length) {
        PrintChars(Chars, index + 1);
      }
    }
  });
}
