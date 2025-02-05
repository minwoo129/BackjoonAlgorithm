import Foundation

func solution(_ numbers:[Int], _ direction:String) -> [Int] {
    let count:Int = numbers.count
    if(direction == "right") {
        return (0..<count).map { numbers[($0 + (count-1)) % count] };
    }
    else {
        return (0..<count).map { numbers[($0 + 1) % count] }
    }
}