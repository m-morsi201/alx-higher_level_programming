#!/usr/bin/node
// Script that computes the number of tasks completed by user id.
const request = require('request');
// The first argument is the API URL.
const ApiUrl = process.argv[2];
request(ApiUrl, (error, response, body) => {
  const comp = {};
  if (error) {
    console.log(error);
  }
  const Json = JSON.parse(body);
  Json.forEach(element => {
    if (element.completed) {
      if (!comp[element.userId]) {
        comp[element.userId] = 0;
      }
      comp[element.userId]++;
    }
  });
  console.log(comp);
});
