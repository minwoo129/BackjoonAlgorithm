const fs = require('fs');
let inputs = fs.readFileSync('/dev/stdin').toString().split(' ');
let num = parseInt(inputs[0]);

let i = 2;
let primes = [];
while(true) {
    if(num%i === 0) {
        num /= i;
        primes.push(i);
        i = 1;
    }
    i++;
    if(i > num) break;
}
console.log(primes.join('\n'));