class Solution {
    fun solution(my_string: String): Int {
        var answer: Int = 0
        var type:String = "";
        
        val arr = my_string.split(" ").toTypedArray();
        
        for(str in arr) {
            if(str == "+" || str == "-") type = str;
            else {
                if(type == "-") answer -= str.toInt();
                else answer += str.toInt();
            }
        }
        
        return answer
    }
}