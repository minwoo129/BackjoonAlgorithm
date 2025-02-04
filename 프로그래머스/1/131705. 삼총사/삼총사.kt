class Solution {
    fun solution(number: IntArray): Int {
        var answer: Int = 0
        var check = Array(number.size) { true }
        
        fun DFS(L: Int, idx: Int) {
            if(L == 3) {
                var sum = 0
                for(i in 0 until number.size) {
                    if(!check[i]) {
                        sum += number[i];
                    }
                }
                
                if(sum == 0) answer++
            }
            else {
                for(i in idx until number.size) {
                    if(check[i]) {
                        check[i] = false;
                        DFS(L+1, i+1);
                        check[i] = true;
                    }
                }
            }
        }
        
        DFS(0, 0)
        return answer
    }
}