class Solution {
    fun solution(s: String, skip: String, index: Int): String {
        var answer: String = ""
        var ascii_a = 'a'.toInt();
        var dics = List(26) {i -> (ascii_a+i).toChar() };
        dics = dics.filterNot { skip.contains(it) };
        
        for(ch in s) {
            var idx = dics.indexOf(ch);
            idx = (idx + index) % dics.size;
            answer += dics[idx];
        }
        return answer
    }
}