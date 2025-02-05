import Foundation

func solution(_ s:String) -> Int {
    var splits = s.split(separator: " ");
    var last:Int = 0;
    var sum:Int = 0;
    
    for ch in splits {
        if(ch == "Z") {
            sum -= last;
            last = 0
        }
        else {
            var num = Int(ch)!;
            last = num;
            sum += last
        }
        
    }
    return sum
}