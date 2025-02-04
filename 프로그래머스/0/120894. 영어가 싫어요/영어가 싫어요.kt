class Solution {
    fun solution(numbers: String): Long {
        var answer: Long = 0
        var nums = numbers;
        val numberHash:Map<String, Int> = mapOf(
            "zero" to 0,
            "one" to 1, 
            "two" to 2, 
            "three" to 3, 
            "four" to 4, 
            "five" to 5, 
            "six" to 6, 
            "seven" to 7, 
            "eight" to 8, 
            "nine" to 9
        )
        
        while(nums.length > 0) {
           for(entry in numberHash) {
               if(nums.indexOf(entry.key) == 0) {
                   answer *= 10;
                   answer += entry.value
                   nums = nums.substring(entry.key.length)
               }
           }
        }
        
        return answer
    }
}