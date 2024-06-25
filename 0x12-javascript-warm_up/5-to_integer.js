#!/usr/bin/node
// script that prints My number: <first argument converted in integer>
const myNam = parseInt(process.argv[2], 10);
if (Number.isInteger(myNam)) {
  console.log('My number: ' + myNam);
} else {
  console.log('Not a number');
}
