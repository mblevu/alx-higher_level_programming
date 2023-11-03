#!/usr/bin/node
// script that fetches and replaces the name of this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
  $('DIV#character').text(data.name);
});
