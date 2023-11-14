#!/usr/bin/node

const SquareParent = require('./5-square');

class Square extends SquareParent {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    if (typeof (c) === 'undefined') {
      c = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      console.log(c.repeat(this.size));
    }
  }
}

module.exports = Square;
