#!/usr/bin/node
const fs = require('fs');

if (process.argv.length !== 4) {
  console.log('Usage: ./1-writeme.js <file path> <text to write>');
  process.exit(1);
}
const filePath = process.argv[2];
const text = process.argv[3];

fs.writeFile(filePath, text, 'utf-8', (err) => {
  if (err) {
    console.log(err);
    process.exit(1);
  }
});
