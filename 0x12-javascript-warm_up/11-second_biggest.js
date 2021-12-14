#!/usr/bin/node
'use strict';
let nextMax = 0;
let args = process.argv.slice(2);
if (args.length < 1 || args.length === 1){
    console.log(0);
} else{
    args.sort();
    nextMax = args[args.length - 2];
}
console.log(nextMax);