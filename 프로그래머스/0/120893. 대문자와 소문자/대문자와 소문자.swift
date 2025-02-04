import Foundation

func solution(_ my_string:String) -> String {
    var result:String = "";
    let diff = UInt8(32)
    for ch in my_string {
        var ascii = ch.asciiValue!;
        if(String(ch) >= "a") {
            ascii -= diff;
        }
        else {
            ascii += diff;
        }
        var str = String(UnicodeScalar(UInt8(ascii)));
        result += str;
    }
    return result
}