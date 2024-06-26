#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments.
const nums = process.argv.splice(2, process.argv.length);
function descendingOrder (arr) {
  return (arr.sort().reverse());
}
const orderNums = descendingOrder(nums);
if (orderNums <= 1) {
  console.log('0');
} else {
  console.log(orderNums[1]);
}
