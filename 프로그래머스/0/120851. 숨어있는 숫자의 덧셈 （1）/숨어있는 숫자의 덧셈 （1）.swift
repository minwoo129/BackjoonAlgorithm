import Foundation

func solution(_ my_string:String) -> Int {
    var result:Int = 0;
    
    for ch in my_string {
        if(ch == "1") {
            result += 1
        }
        else if(ch == "2") {
            result += 2
        }
        else if(ch == "3") {
            result += 3
        }
        else if(ch == "4") {
            result += 4
        }
        else if(ch == "5") {
            result += 5
        }
        else if(ch == "6") {
            result += 6
        }
        else if(ch == "7") {
            result += 7
        }
        else if(ch == "8") {
            result += 8
        }
        else if(ch == "9") {
            result += 9
        }
        else {
            result += 0
        }
    }
    return result
}