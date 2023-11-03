#!/usr/bin/node
// script that updates the text color of the HTML tag HEADER to red (#FF0000)
$(document).ready(function () {
  $('DIV#red_header').click(function () {
    $('header').addClass('red');
  });
});
