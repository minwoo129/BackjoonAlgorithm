import Foundation

func solution(_ n:Int, _ k:Int) -> Int {
    let freeJuice: Int = n / 10;
    let price: Int = (n*12000) + (k-freeJuice)*2000;
    return price;
}