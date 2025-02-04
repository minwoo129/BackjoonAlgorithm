class Solution {
    fun solution(array: IntArray): IntArray {
        var answer: IntArray = intArrayOf()
        var num:Int = 0;
        var idx:Int = -1;
        
        for(i in 0..array.size-1) {
            if(array[i] > num) {
                num = array[i];
                idx = i;
            }
        }
        
        answer = intArrayOf(num, idx);
        return answer
    }
}