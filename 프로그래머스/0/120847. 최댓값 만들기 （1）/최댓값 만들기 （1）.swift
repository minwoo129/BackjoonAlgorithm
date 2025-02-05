import Foundation

func solution(_ numbers:[Int]) -> Int {
    var sortedArr = numbers.sorted(by: >);
    return sortedArr[0] * sortedArr[1]
}