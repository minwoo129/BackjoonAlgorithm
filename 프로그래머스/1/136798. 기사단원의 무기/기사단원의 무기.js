function getPrimes(number) {
    let primes = Array.from({length: number+1}, () => true);
    primes[0] = primes[1] = false;
    
    for(let i = 2; i*i <= number; i++) {
        if(primes[i]) {
            for(let j = i*i; j <= number; j += i) primes[j] = false;
        }
    }
    
    return primes;
    
}

function solution(number, limit, power) {
    var answer = 0;
    let counts = [];
    
    for(let i = 1; i <= number; i++) {
        let count = 0
        for(let j = 1; j <= i/2; j++) {
            if(i % j === 0) {
                count += 1;
            }
        }
        
        counts.push(count+1);
    }
    
    
    answer = counts.reduce((result, item) => {
        result += (item > limit ? power : item);
        return result;
    }, 0)
    return answer;
}