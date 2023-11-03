#!/usr/bin/node
// script that fetches and replaces the name of this URL: https://fourtonfish.com/hellosalut/?lang=fr
$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const langCode = $('INPUT#language_code').val();
    $.get(`https://fourtonfish.com/hellosalut/?lang=${langCode}`, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });

  $('INPUT#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      $('INPUT#btn_translate').click();
    }
  });
});
