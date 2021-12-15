#!/usr/bin/node
let dict = require('./100-data.js').dict;
let newDict = {};
for (let key in dict){
    if (newDict[dict[key]] === undefined){
        newDict[dict[key]] = [];
    }
    newDict[dict[key]].push(key);
}
console.log(newDict);