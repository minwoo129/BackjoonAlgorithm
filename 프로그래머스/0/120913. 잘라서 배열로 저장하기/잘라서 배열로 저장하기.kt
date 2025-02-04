class Solution {
    fun solution(my_str: String, n: Int): Array<String> {
        var answer: Array<String> = arrayOf<String>()
        var count = my_str.length/n;
        
        if(my_str.length%n != 0) count++;
        
        for(i in 0..count-1) {
            var startIdx = i * n;
            var endIdx = i*n + n;
            
            if(i == count-1) {
                endIdx = my_str.length;
            }
            
            answer += my_str.slice(startIdx until endIdx)
        }
        return answer
    }
}