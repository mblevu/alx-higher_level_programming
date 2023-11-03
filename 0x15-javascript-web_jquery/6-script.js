#!/usr/bin/node
// script that updates the text color of the HTML tag HEADER to red (#FF0000)
$(document).ready(function () {
  $('DIV#update_header').click(function () {
    $('header').text('New Header!!!');
  });
});
