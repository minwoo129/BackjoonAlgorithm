import Foundation

func solution(_ letter:String) -> String {
    let mource: [String:String] = [".-":"a","-...":"b","-.-.":"c","-..":"d",".":"e","..-.":"f",
    "--.":"g","....":"h","..":"i",".---":"j","-.-":"k",".-..":"l",
    "--":"m","-.":"n","---":"o",".--.":"p","--.-":"q",".-.":"r",
    "...":"s","-":"t","..-":"u","...-":"v",".--":"w","-..-":"x",
    "-.--":"y","--..":"z"];
    var message:String = "";
    var messageArr = letter.split(separator: " ");
    
    for ch in messageArr {
        message += (mource[String(ch)]!);
    }
    
    
    return message
}