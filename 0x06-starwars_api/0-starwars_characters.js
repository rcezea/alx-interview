#!/usr/bin/node
const request = require('request');

let url = `https://swapi-api.alx-tools.com/api/films/` + process.argv[2];

request(url, function (err, res, body) {
	if (err) {
		console.error(err);
		return;
	}

	let actors = JSON.parse(body).characters;

	let i = 0;
	while (i < actors.length) {
		request(actors[i], function (err, res, body) {
			if (err) {
				console.error(err);
				return;
			}
			console.log(JSON.parse(body).name);
		});
		i++;
	}
});
