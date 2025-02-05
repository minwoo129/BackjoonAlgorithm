import Foundation

func solution(_ rsp:String) -> String {
    let rspDics: [String:String] = ["2":"0", "0":"5", "5":"2"];
    var result:String = "";
    for ch in rsp {
        result += rspDics[String(ch)]!;
    }
    return result
}