#!/usr/bin/node
const Rectangle = require('./4-rectangle');
// Import the Rectangle class.
class Square extends Rectangle {
  // Constructor of the Square class.
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
