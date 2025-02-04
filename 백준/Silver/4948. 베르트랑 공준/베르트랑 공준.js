const fs = require("fs");
let rawInputs = fs.readFileSync("/dev/stdin").toString().split("\n").map(num => parseInt(num));
const limit = 123456*2;
let primes = Array.from({length: limit+1}, () => true);
primes[0] = primes[1] = false;
for(let i = 2; i*i <= limit; i++) {
    if(primes[i]) {
        for(let j = i*i; j <= limit; j+=i) primes[j] = false;
    }
}

function getPrimeCnt(num) {
    let cnt = 0;
    for(let i = num+1; i <= num*2; i++) {
        if(primes[i]) cnt++;
    }
    return cnt;
}

for(let i = 0; i < rawInputs.length; i++) {
    if(rawInputs[i] == 0) break;
    console.log(getPrimeCnt(rawInputs[i]));
}