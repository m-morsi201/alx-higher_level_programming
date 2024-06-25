#!/usr/bin/node
// script that prints x times “C is fun”
const xTimes = parseInt(process.argv[2], 10);
if (!Number.isInteger(xTimes)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < xTimes; i++) {
    // in for loop to handel negative case I used (i < xTimes).
    console.log('C is fun');
  }
}
