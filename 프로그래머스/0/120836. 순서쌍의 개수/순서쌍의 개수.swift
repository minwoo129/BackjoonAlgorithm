import Foundation

func solution(_ n:Int) -> Int {
    var count:Int = 0;
    for i in 1...n {
        count += (n%i == 0) ? 1 : 0
    }
    return count
}