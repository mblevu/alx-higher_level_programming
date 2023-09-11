#!/usr/bin/node

function secondBiggest (args) {
  const numbers = args.map(arg => parseInt(arg)).filter(Number.isInteger);

  if (numbers.length < 2) {
    return 0;
  }

  numbers.sort((a, b) => b - a);
  return numbers[1];
}

const args = process.argv.slice(2);
const result = secondBiggest(args);

console.log(result);
