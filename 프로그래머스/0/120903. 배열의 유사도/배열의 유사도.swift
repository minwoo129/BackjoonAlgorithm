import Foundation

func solution(_ s1:[String], _ s2:[String]) -> Int {
    var count:Int = 0;
    
    for s in s1 {
        if(s2.contains(s)) {
            count += 1;
        }
    }
    return count;
}