#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, async (err, res) => {
  err && console.log(err);

  const charactersArray = (JSON.parse(res.body).characters);
  for (const character of charactersArray) {
    await new Promise((resolve) => {
      request(character, (err, res, body) => {
        err && console.log(err);

        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
