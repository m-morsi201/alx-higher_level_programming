#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments.
const nums = process.argv.splice(2, process.argv.length);
function descendingOrder (arr) {
  return (arr.sort().reverse());
}
const orderNums = descendingOrder(nums);
console.log(orderNums[1]);
