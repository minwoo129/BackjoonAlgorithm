import Foundation

func solution(_ cipher:String, _ code:Int) -> String {
    var result:String = "";
    var pos:Int = 0;
    
    for ch in cipher {
        pos += 1;
        if(pos % code == 0) {
            result += String(ch);
        }
    }
    return result
}