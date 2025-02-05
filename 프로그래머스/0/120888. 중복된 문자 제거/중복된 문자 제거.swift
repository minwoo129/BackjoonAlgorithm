import Foundation

func solution(_ my_string:String) -> String {
    var chArr: [String] = [];
    for ch in my_string {
        let newCh = String(ch);
        
        if(!chArr.contains(newCh)) {
            chArr.append(newCh)
        }
    }
    
    return chArr.joined(separator: "")
}