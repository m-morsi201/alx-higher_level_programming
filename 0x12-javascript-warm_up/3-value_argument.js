#!/usr/bin/node
// script that prints the first argument passed to it
const argvNum = process.argv;
if (argvNum[2]) {
  console.log(argvNum[2]);
} else {
  console.log('No argument');
}
