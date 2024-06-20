#!/usr/bin/node
class Rectangle {
  // Constructor of the Rectangle class.
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    // method called print() that prints the rectangle using the character X.
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s += 'X';
      }
      console.log(s);
    }
  }

  rotate () {
    // method called rotate() that exchanges the width and the height of the rectangle.
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    // method called double() that multiples the width and the height of the rectangle by 2.
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
