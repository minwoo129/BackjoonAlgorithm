class Solution {
    fun solution(ingredient: IntArray): Int {
        var answer: Int = 0
        var sb = StringBuilder()
        
        for(num in ingredient) {
            sb.append(num.toString());
            if(sb.length >= 4 && (sb.substring(sb.length-4) == "1231")) {
                answer++;
                sb.setLength(sb.length-4)
            }
        }
        return answer
    }
}