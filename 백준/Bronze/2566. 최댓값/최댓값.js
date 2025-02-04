const fs = require("fs");
let inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
let nums = [];
for(let i = 0; i < inputs.length; i++) {
    nums = [ ...nums, ...inputs[i].trim().split(' ').map(num => parseInt(num)) ];
}
const max = Math.max(...nums);
const maxIdx = nums.findIndex(item => item == max);

console.log(max);
console.log(`${Math.floor(maxIdx/9)+1} ${maxIdx%9+1}`)

