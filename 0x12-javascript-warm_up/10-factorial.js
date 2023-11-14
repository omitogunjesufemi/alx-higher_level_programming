#!/usr/bin/node

const argv = process.argv;

function factorial (digit) {
  if (digit === 0) {
    return (1);
  }
  return (digit * factorial(digit - 1));
}

if (argv.length === 3 && !isNaN(argv[2])) {
  console.log(factorial(Number(argv[2])));
} else {
  console.log(1);
}
