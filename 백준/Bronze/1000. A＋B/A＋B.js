const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim()

const [a, b] = input.split(" ")

sum = parseInt(a) + parseInt(b)
console.log(sum)