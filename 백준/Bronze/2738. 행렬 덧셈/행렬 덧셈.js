const fs = require("fs");
let rawInputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [n, m] = rawInputs.shift().split(' ').map(item => parseInt(item));

for(let i = 0; i < n; i++) {
    let sums = [];
    let arrA = rawInputs[i].split(' ').map(num => parseInt(num));
    let arrB = rawInputs[n+i].split(' ').map(num => parseInt(num));
    for(let j = 0; j < m; j++) {
        sums.push(arrA[j] + arrB[j]);
    }
    console.log(sums.join(' '));
}
