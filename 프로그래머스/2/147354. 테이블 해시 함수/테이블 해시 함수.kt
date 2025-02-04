class Solution {
    fun solution(data: Array<IntArray>, col: Int, row_begin: Int, row_end: Int): Int {
        var answer: Int = 0
        var dataList = MutableList(data.size, { i -> data[i].toMutableList() })
        dataList.sortWith(compareBy({ it[col-1] },{ -it[0] }))
        
        for(i in row_begin..row_end) {
            var S = 0
            for(n in dataList[i-1]) {
                S += (n % i);
            }
            
            if(answer == 0) {
                answer = S;
            }
            else {
                answer = answer xor S
            }
        }
        return answer
    }
}