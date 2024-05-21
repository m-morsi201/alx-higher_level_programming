#!/usr/bin/node
//script that reads and prints the content of a file.
const process = require('process');
const fs = require('fs');
// The first argument is the file path.
const file = process.argv[2];
// The content of the file must be read in utf-8.
fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data.toString());
  }
});
