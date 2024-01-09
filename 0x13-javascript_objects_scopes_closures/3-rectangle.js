#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      // If w or h is 0 or not a positive integer, create an empty object
      return {};
    }

    this.width = w;
    this.height = h;
  }

  print () {
    // Method to print the rectangle using the character X
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
