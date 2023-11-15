#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;

fs.readFile(argv[2], (err, data) => {
  if (err) {
    console.error(err);
  }

  fs.writeFile(argv[4], data, (err) => {
    if (err) {
      console.error(err);
    }
  });
});

fs.readFile(argv[3], (err, data) => {
  if (err) {
    console.error(err);
  }

  fs.appendFile(argv[4], data, (err) => {
    if (err) {
      console.error(err);
    }
  });
});
