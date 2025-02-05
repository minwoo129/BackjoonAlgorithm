import Foundation

func solution(_ num_list:[Int]) -> [Int] {
    var even:Int = 0;
    var odd:Int = 0;
    for num in num_list {
        if(num%2 == 0) {
            even += 1;
        }
        else {
            odd += 1;
        }
    }
    return [even, odd]
}