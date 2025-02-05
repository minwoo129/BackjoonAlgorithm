class Solution {
    fun solution(board: Array<IntArray>): Int {
        
        var bombs: Array<IntArray> = arrayOf();
        var height = board.size
        var width = board[0].size;
        var answer: Int = width * height
        
        var map = MutableList(height, {i -> board[i].toMutableList()})
        
        for(i in 0 until height) {
            for(j in 0 until width) {
                if(board[i][j] == 1) {
                    bombs += intArrayOf(i, j);
                }
            }
        }
        
        val areas = arrayOf(
            intArrayOf(-1, -1), 
            intArrayOf(-1, 0), 
            intArrayOf(-1, 1), 
            intArrayOf(0, -1), 
            intArrayOf(0, 1),
            intArrayOf(1, -1),
            intArrayOf(1, 0),
            intArrayOf(1, 1)
        )
        
        for(point in bombs) {
            var x = point[1];
            var y = point[0];
            answer--;
            for(a in areas) {
                var dx = x + a[1];
                var dy = y + a[0];
                if(dx >= 0 && dx < width && dy >= 0 && dy < height && map[dy][dx] == 0) {
                    map[dy][dx] = 1
                    answer--
                }
            }
        }
        
        return answer
    }
}