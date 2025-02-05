import Foundation

func solution(_ num_list:[Int], _ n:Int) -> [[Int]] {
    return stride(from: 0, to: num_list.count, by: n).map {
        Array(num_list[$0..<min($0+n, num_list.count)])
    }
}