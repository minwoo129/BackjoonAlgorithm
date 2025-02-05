import Foundation

func solution(_ dot:[Int]) -> Int {
    let (x,y) = (dot[0], dot[1]);
    
    if(x > 0) {
        if(y > 0) {
            return 1
        }
        else {
            return 4
        }
    }
    else {
        if(y > 0) {
            return 2
        }
        else {
            return 3
        }
    }
}