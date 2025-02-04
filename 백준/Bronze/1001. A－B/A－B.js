const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim()

const [a, b] = input.split(" ")

console.log(parseInt(a) - parseInt(b))