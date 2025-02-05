import Foundation

func solution(_ emergency:[Int]) -> [Int] {
    var dics = [Int:Int]();
    var sortedEmergencys = emergency;
    var count:Int = 1;
    var answer:[Int] = [];
    sortedEmergencys.sort {(a,b) -> Bool in return a>b}
    
    
    for i in sortedEmergencys {
        dics[i] = count;
        count += 1;
    }
    
    return emergency.map {dics[$0]!}
}