import Foundation

func solution(_ my_string:String, _ n:Int) -> String {
    var answer:String = ""
    for str in my_string {
        answer += String(repeating:str, count: n);
    }
    return answer;
}