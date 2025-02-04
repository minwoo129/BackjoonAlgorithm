const fs = require('fs');
let inputs = fs.readFileSync('/dev/stdin').toString().split('\n');
const m = parseInt(inputs[0]);
const n = parseInt(inputs[1]);

function setPrimes(maxNum) {
    let primeDatas = Array.from({length: maxNum+1}, () => true);
    primeDatas[0] = primeDatas[1] = false;
    for(let i = 2; i*i <= maxNum; i++) {
        if(primeDatas[i]) {
            for(let j = i*i; j <= maxNum; j+=i) primeDatas[j] = false
        }
    }
    return primeDatas
}

const primes = setPrimes(n);
let primeNums = [];
for(let i = m; i <= n; i++) {
    if(primes[i]) primeNums.push(i);
}

if(primeNums.length === 0) {
    console.log(-1);
}
else {
    const sum = primeNums.reduce((a,b) => a+b);
    const min = Math.min(...primeNums);
    console.log(sum);
    console.log(min)
}