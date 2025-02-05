import Foundation

func solution(_ age:Int) -> String {
    var answer = "";
    for i in String(age) {
        if(i == "0") {
            answer.append("a");
        }
        else if(i == "1") {
            answer.append("b");
        }
        else if(i == "2") {
            answer.append("c");
        }
        else if(i == "3") {
            answer.append("d");
        }
        else if(i == "4") {
            answer.append("e");
        }
        else if(i == "5") {
            answer.append("f");
        }
        else if(i == "6") {
            answer.append("g");
        }
        else if(i == "7") {
            answer.append("h");
        }
        else if(i == "8") {
            answer.append("i");
        }
        else {
            answer.append("j")
        }
    }
    return answer;
}