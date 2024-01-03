#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) return;
  const todos = JSON.parse(body);
  const uwct = {};

  for (const todo of todos) {
    if (todo.completed === true) {
      if (uwct[todo.userId + ''] === undefined) uwct[todo.userId + ''] = 1;
      else uwct[todo.userId + ''] = uwct[todo.userId + ''] + 1;
    }
  }
  console.log(uwct);
});
