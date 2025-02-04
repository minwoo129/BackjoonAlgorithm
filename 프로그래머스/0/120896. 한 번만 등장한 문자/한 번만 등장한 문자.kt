class Solution {
    fun solution(s: String): String {
        var answer: String = ""
        val arr = IntArray(26);
        
        for(i in 0..25) arr[i] = 0;
        for(e in s) {
            arr[e.code-97] += 1;
        }
        for(i in 0..25) {
            if(arr[i] == 1) {
                answer += (i+97).toChar();
            }
        }
        return answer
    }
}