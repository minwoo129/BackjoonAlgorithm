import Foundation

func solution(_ n:Int, _ t:Int) -> Int {
    var result:Int = n;
    
    for i in 1...t {
        result *= 2;
    }
    return result
}