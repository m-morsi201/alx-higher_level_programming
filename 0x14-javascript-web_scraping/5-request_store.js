#!/usr/bin/node
// Script that gets the contents of a webpage and stores it in a file.
const request = require('request');
const fs = require('fs');
// The first argument is the Url to request.
const Url = process.argv[2];
// The second argument the file path to store the body response
const Resp = process.argv[3];

request(Url, (error, response, body) => {
  if (error == null) {
    fs.writeFileSync(Resp, body);
  }
});
