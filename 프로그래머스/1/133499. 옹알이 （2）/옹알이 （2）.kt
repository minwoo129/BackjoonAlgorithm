class Solution {
    fun solution(babbling: Array<String>): Int {
        var answer: Int = 0
        val saids = arrayOf("aya", "ye", "woo", "ma");
        
        for(str in babbling) {
            var temp = str;
            for(i in 0 until saids.size) {
                if(temp.contains(saids[i]+saids[i])) {
                    continue;
                }
                else {
                    temp = temp.replace(saids[i], " ");
                }
            }
            
            if(temp.replace(" ", "") == "") answer++;
        }
        
        return answer
    }
}