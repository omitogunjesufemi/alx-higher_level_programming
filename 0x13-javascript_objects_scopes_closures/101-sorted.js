#!/usr/bin/node
const dict = require('./101-data').dict;
const allVal = Object.values(dict);

function checkForReplica (list) {
  const newList = [];
  for (let i = 0; i < list.length; i++) {
    if (!(list[i] in newList)) {
      newList.push(list[i]);
    }
  }
  return (newList);
}

const valList = checkForReplica(allVal);
const newDict = {};

for (let i = 0; i < valList.length; i++) {
  newDict[valList[i]] = [].sort((a, b) => b - a);
}

Object.entries(dict).forEach(entry => {
  const [key, value] = entry;

  for (let i = 0; i < valList.length; i++) {
    if (value === valList[i]) {
      newDict[String(value)].push(key);
    }
  }
});

console.log(newDict);
