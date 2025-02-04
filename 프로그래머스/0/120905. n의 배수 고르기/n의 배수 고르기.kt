class Solution {
    fun solution(n: Int, numlist: IntArray): IntArray {
        var answer: IntArray = intArrayOf()
        
        for(num in numlist) {
            if(num % n == 0) {
                answer += num;
            }
        }
        return answer
    }
}