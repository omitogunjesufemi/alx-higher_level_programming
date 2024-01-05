#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];

if (!filePath) {
  console.log('file does not exist');
  process.exit(1);
}

fs.readFile(`./${filePath}`, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
    process.exit(1);
  }
  console.log(data);
});
