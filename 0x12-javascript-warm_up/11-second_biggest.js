#!/usr/bin/node
const argv = process.argv;

if (argv.length > 3) {
  const newArgv = [];
  for (let i = 2; i < argv.length; i++) {
    newArgv.push(+argv[i]);
  }
  newArgv.sort(function (a, b) {
    return (b - a);
  });
  console.log(newArgv[1]);
} else {
  console.log(0);
}
