#!/usr/bin/node
// script that writes a string to a file.
const process = require('process');
const fs = require('fs');

// The first argument is the file path.
const FilePath = process.argv[2];
// The second argument is the string to write.
const text = process.argv[3];

fs.writeFile(FilePath, text, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  }
});
