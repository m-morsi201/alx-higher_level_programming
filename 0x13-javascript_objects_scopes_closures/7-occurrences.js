#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  // function to count number of occurrences in a list.
  let count = 0;
  list.forEach((item) => {
    if (item === searchElement) {
      count++;
    }
  });
  return count;
};
