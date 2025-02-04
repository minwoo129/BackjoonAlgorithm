class Solution {
    fun solution(n: Int, m: Int, section: IntArray): Int {
        var answer: Int = 0
        var walls = Array(n+1) { 1 };
        var newSections = intArrayOf();
        
        for(idx in section) {
            walls[idx] = 0;
            newSections += idx;
        }
        
        var currentIdx = 0;
        
        while(currentIdx < walls.size) {
            if(walls[currentIdx] == 0) {
                answer++;
                currentIdx += m
            }
            else {
                currentIdx++;
            }
        }
        return answer
    }
}