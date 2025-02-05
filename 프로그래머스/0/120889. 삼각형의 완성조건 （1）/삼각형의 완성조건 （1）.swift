import Foundation

func solution(_ sides:[Int]) -> Int {
    var sortedArr = sides.sorted(by:<);
    let maxLength = sortedArr.popLast() ?? 0;
    let sumLeft = sortedArr.reduce(0) {(result, item) -> Int in return result + item};
    
    return ((maxLength < sumLeft) ? 1 : 2);
}