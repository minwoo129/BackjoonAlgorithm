class Solution {
    fun solution(a: Int, b: Int, n: Int): Int {
        var answer: Int = 0
        var left = n;
        
        while(left >= a) {
            var getCnt = left/a;
            left = left - (a * getCnt) + (getCnt*b);
            answer += (getCnt*b)
            
        }
        
        
        return answer
    }
}