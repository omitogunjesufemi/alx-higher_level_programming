#!/usr/bin/node
exports.converter = function (base) {
  return function (digit) {
    return (digit.toString(base));
  };
};
