#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments.
const nums = process.argv.splice(2, process.argv.length).reverse();
console.log(nums[1]);
