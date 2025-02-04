import Foundation

func solution(_ order:Int) -> Int {
    var num = order;
    var count = 0;
    
    while num != 0 {
        let orderNum = num % 10;
        count += ((orderNum == 3) || (orderNum == 6) || (orderNum == 9)) ? 1 : 0;
        num /= 10;
    }
    return count;
}