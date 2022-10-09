#!/usr/bin/node

let item1 = 0;
exports.logMe = function (item) {
  console.log(item1 + ': ' + item);
  item1++;
};
