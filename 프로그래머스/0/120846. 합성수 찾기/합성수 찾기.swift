import Foundation

func solution(_ n:Int) -> Int {
    var count:Int = 0;
    
    if n < 4 {
        return 0;
    }
    var primes = [Bool](repeating: true, count: 101);
    primes[0] = false;
    primes[1] = false;
    
    var idx = 2;
    while Int(pow(Double(idx), 2)) < 101 {
        if(primes[idx]) {
            for i in stride(from: idx*idx, to: 101, by: idx) {
                primes[i] = false
            }
            
        }
        idx += 1;
    }
    

    for i in 2...n {
        count += (!primes[i] ? 1 : 0)
    }
    return count
}