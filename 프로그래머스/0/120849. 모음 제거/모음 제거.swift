import Foundation

func solution(_ my_string:String) -> String {
    var result:String = "";
    
    for ch in my_string {
        if !(ch == "a" || ch == "e" || ch == "i" || ch == "o" || ch == "u") {
            result += String(ch);
        }
    }
    return result
}