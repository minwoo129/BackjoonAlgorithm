class Solution {
    fun solution(my_string: String): String {
        var answer: String = ""
        var str = my_string.toLowerCase();
        var strArr = str.toCharArray().sortedArray();
        
        answer = String(strArr);
        
        return answer
    }
}