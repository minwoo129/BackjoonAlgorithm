import Foundation

func solution(_ n:Int) -> [Int] {
    var answer: [Int] = [];
    var num = n;
    var count = 2;
    
    for i in 2...n {
        if(n % i == 0 && !answer.contains(where: {i % $0 == 0})) {
            answer.append(i)
        }
    }
    
    
    return answer;
}