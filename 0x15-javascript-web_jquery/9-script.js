#!/usr/bin/node
// script that fetches and replaces the name of this URL: https://fourtonfish.com/hellosalut/?lang=fr
const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

$.get(url, function (data) {
  $('DIV#hello').text(data.hello);
});
