#!/usr/bin/node
const { argv } = require('node:process');

if (Object.keys(argv).length === 3) {
  console.log('Argument found');
} else if (Object.keys(argv).length > 3) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
