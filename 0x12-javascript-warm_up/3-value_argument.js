#!/usr/bin/node
const { argv } = require('node:process');

let count = 0;
argv.forEach((val, index) => {
    if (index === 2) {
	console.log(val);
    }
    count++;
});

if (count < 3) {
    console.log("No argument");
}
