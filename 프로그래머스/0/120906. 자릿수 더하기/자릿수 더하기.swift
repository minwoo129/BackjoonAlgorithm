import Foundation

func solution(_ n:Int) -> Int {
    var num:Int = n;
    var result:Int = 0;
    
    while num != 0 {
        result += (num%10);
        num /= 10;
    }
    return result
}