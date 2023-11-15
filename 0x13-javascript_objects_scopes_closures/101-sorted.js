#!/usr/bin/node
const dict = require('./101-data').dict;

const result = {};

for (const key in dict) {
  const value = dict[key];

  if (result[value]) {
    result[value].push(key);
  } else {
    result[value] = [key];
  }
}

console.log(result);
