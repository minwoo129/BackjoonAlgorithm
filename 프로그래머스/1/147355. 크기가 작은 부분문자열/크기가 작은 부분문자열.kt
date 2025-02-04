class Solution {
    fun solution(t: String, p: String): Int {
        var answer: Int = 0
        var length = p.length;
        var pNum = p.toLong(); 
        
        for(i in 0..t.length-1) {
            var endIdx = i + length;
            var num = t.substring(i until endIdx).toLong()
            if(num <= pNum) answer++;
            
            if(endIdx == t.length) break;
        }
        return answer
    }
}