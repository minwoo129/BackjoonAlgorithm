class Solution {
    fun solution(num: Int, k: Int): Int {
        var answer: Int = 0;
        var numStr = num.toString();
        var kStr = k.toString();
        if(numStr.contains(kStr)) {
            return numStr.indexOf(kStr)+1;
        }
        else {
            return -1;
        }
    }
}