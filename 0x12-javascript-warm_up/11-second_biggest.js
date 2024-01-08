#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  const numbers = args.map(Number).filter(num => !isNaN(num));
  const uniqueNumbers = [...new Set(numbers)];

  if (uniqueNumbers.length <= 1) {
    console.log(0);
  } else {
    const sortedNumbers = uniqueNumbers.sort((a, b) => b - a);
    console.log(sortedNumbers[1]);
  }
}
