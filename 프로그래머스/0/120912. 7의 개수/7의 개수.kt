class Solution {
    fun solution(array: IntArray): Int {
        var answer: Int = 0
        var joinedStr = ""
        
        for(num in array) {
            joinedStr += num.toString()
        }
        
        var splitArr = joinedStr.toCharArray();
        
        for(ch in splitArr) {
            if(ch == '7') answer++;
        }
        return answer
    }
}