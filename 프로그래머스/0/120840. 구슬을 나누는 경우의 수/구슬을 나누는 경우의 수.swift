import Foundation

func getFact(_ num:Int) -> Double {
    return Double((1...num).reduce(1.0) { Double($0) * Double($1) })
}

func solution(_ balls:Int, _ share:Int) -> Int {
    
    if(balls == share) {
        return 1;
    }
    
    let a:Double = getFact(balls);
    let b:Double = getFact(balls-share);
    let c:Double = getFact(share);
    
    return Int(round(a/(b*c)));
}