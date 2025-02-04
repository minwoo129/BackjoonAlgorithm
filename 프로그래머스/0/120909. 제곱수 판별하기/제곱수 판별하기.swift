import Foundation

func solution(_ n:Int) -> Int {
    var i:Int64 = 1;
    
    while i*i < n {
        i += 1;
    }
    return (i * i == n) ? 1: 2
}