#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    // Calling the constructor of the parent class (Rectangle) using super()
    super(size, size);
  }
}

module.exports = Square;
