#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const movies = JSON.parse(body).results;
    let count = 0;
    for (const movie of movies) {
      for (const character of movie.characters) {
        if (character.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
