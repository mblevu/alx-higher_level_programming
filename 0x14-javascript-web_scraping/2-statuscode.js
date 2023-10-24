#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: ./2-statuscode.js <URL>');
  process.exit(1);
}

const url = process.argv[2];

request(url, (err, res) => {
  if (err) {
    console.log('error:', err);
    process.exit(1);
  }
  console.log('code: ' + res.statusCode);
});
