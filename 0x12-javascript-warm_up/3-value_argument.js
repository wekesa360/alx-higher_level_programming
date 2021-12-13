#!/usr/bin/node
console.log(typeof process.argv[2] === 'udefined' ? 'No argument' : process.argv[2]);