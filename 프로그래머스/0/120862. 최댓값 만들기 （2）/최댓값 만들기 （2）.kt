class Solution {
    fun solution(numbers: IntArray): Int {
        var answer: Int = Integer.MIN_VALUE;
        
        for(i in 0..numbers.size-1) {
            for(j in (i+1)..numbers.size-1) {
                var newValue = numbers[i] * numbers[j];
                
                if(newValue > answer) {
                    answer = newValue
                }
            }
        }
        
        return answer
    }
}