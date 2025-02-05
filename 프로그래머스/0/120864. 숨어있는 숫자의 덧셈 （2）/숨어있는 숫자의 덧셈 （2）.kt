class Solution {
    fun solution(my_string: String): Int {
        var answer: Int = 0
        var str = my_string.replace("[^0-9]".toRegex(), " ");
        var splits = str.split(" ").toMutableList();
        for(v in splits) {
            if(v != "") {
                answer += v.toString().toInt();
            }
        }
        return answer
    }
}