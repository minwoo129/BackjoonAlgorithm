import Foundation

func solution(_ box:[Int], _ n:Int) -> Int {
    var width: Int = box[0] / n;
    var length:Int = box[1] / n;
    var height:Int = box[2] / n;

    return width * length * height
}