import Foundation

func solution(_ my_string:String) -> [Int] {
    var answer:[Int] = [];
    
    for ch in my_string {
        if(String(ch).allSatisfy {$0.isNumber}) {
            answer.append(ch.wholeNumberValue!)
        }
    }
    answer.sort();
    return answer
}