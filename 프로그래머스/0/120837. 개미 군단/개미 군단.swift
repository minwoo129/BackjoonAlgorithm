import Foundation

func solution(_ hp:Int) -> Int {
    var count:Int = 0;
    var leftCnt:Int = hp;
    
    count += (leftCnt/5);
    leftCnt %= 5;
    if leftCnt > 0 {
        count += (leftCnt/3);
        leftCnt %= 3;
        count += leftCnt
    }
    return count
}