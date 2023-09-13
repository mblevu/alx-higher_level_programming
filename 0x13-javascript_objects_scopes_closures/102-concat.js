#!/usr/bin/node

const fs = require('fs');

const fArg = fs.readFileSync(process.argv[2]).toString();
const sArg = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], fArg + sArg);

// const fs = require('fs');

// if (process.argv.length !== 5) {
//   console.error('Usage: node concat-files.js <file1> <file2> <destination>');
//   process.exit(1);
// }

// const sourceFile1 = process.argv[2];
// const sourceFile2 = process.argv[3];
// const destinationFile = process.argv[4];

// fs.readFile(sourceFile1, 'utf8', (err, data1) => {
//   if (err) {
//     console.error(`Error reading ${sourceFile1}: ${err}`);
//     process.exit(1);
//   }

//   fs.readFile(sourceFile2, 'utf8', (err, data2) => {
//     if (err) {
//       console.error(`Error reading ${sourceFile2}: ${err}`);
//       process.exit(1);
//     }

//     const concatenatedData = data1 + data2;

//     fs.writeFile(destinationFile, concatenatedData, 'utf8', (err) => {
//       if (err) {
//         console.error(`Error writing to ${destinationFile}: ${err}`);
//         process.exit(1);
//       }

//       console.log(`Concatenated ${sourceFile1} and ${sourceFile2} to ${destinationFile}`);
//     });
//   });
// });
