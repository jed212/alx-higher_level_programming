#!/usr/bin/node

let count = 0;

exports.logMe = function (item) {
  // Function to print the number of arguments already printed and the new argument value
  console.log(`${count}: ${item}`);
  count++;
};
