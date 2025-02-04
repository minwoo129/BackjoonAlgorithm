const fs = require('fs');
let rawInputs = fs.readFileSync('/dev/stdin').toString().split('\n');
const testCase = parseInt(rawInputs[0]);
const numbers = rawInputs[1].split(' ').map((num) => parseInt(num));
const maxNum = Math.max(...numbers);
let primes = Array.from({length: maxNum+1}, () => true);
primes[0] = false;
primes[1] = false;
for(let i = 2; i*i <= maxNum; i++) {
    if(primes[i]) {
        for(let j = i*i; j <= maxNum; j+= i) primes[j] = false;
    }
}
let cnt = 0;
for(let i = 0; i < numbers.length; i++) {
    if(primes[numbers[i]]) cnt++;
}
console.log(cnt)