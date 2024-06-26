#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments.
const args = process.argv.splice(2, process.argv.length);
const ints = [];
for (let i = 0; i < args.length; i++) {
  ints.push(parseInt(args[i]));
}
const descInts = ints.sort(function (a, b) {
  return (b - a);
});
if (descInts.length <= 1) {
  console.log('0');
} else {
  console.log(descInts[1]);
}
