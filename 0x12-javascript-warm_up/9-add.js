#!/usr/bin/node

const argv = process.argv;

function add (a, b) {
  return (Number(a) + Number(b));
}

if (argv.length === 4 && !isNaN(argv[2]) && !isNaN(argv[3])) {
  console.log(add(argv[2], argv[3]));
} else {
  console.log(NaN);
}
