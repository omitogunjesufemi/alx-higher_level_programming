const list = require('./100-data').list;
const newList = list.map((elem, index) => elem * index);

console.log(list);
console.log(newList);
