#!/usr/bin/node
// script that prints a message depending of the number of arguments passed
const argNum = process.argv.length - 2;
if (argNum === 0) {
  console.log('No argument');
} else if (argNum === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
