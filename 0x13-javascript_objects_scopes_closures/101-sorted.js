#!/usr/bin/node

const inputDict = require('./101-data').dict;

function invertDictionary(inputDict) {
  const outputDict = {};

  for (const userId in inputDict) {
    const occurrences = inputDict[userId];

    if (!outputDict[occurrences]) {
      outputDict[occurrences] = [userId];
    } else {
     
      outputDict[occurrences].push(userId);
    }
  }

  return outputDict;
}

const invertedDict = invertDictionary(inputDict);
console.log(invertedDict);
