import Foundation

func solution(_ array:[Int], _ n:Int) -> Int {
    var diff = 1000;
    var answer:Int = 0
    
    for num in array {
        let newDiff = abs(num-n)
        if(diff > newDiff) {
            diff = newDiff;
            answer = num;
        }
        else if (diff == newDiff) {
            if(answer > num) {
                answer = num
            }
        }
    }
    return answer
}