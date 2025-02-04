class Solution {
    fun solution(wallpaper: Array<String>): IntArray {
        var answer: IntArray = intArrayOf()
        val map = Array(wallpaper.size, {i -> wallpaper[i].toCharArray()});
        var xArr: IntArray = intArrayOf();
        var yArr: IntArray = intArrayOf();
        var lux = 0
        var luy = 0
        var rdx = 0
        var rdy = 0;
        
        for(i in 0..map.size-1) {
            for(j in 0..map[i].size-1) {
                if(map[i][j] == '#') {
                    xArr += j;
                    yArr += i
                }
            }
        }
        
        lux = xArr.minOrNull() ?: 0;
        luy = yArr.minOrNull() ?: 0;
        rdx = xArr.maxOrNull() ?: 0;
        rdy = yArr.maxOrNull() ?: 0;
        
        rdx += 1;
        rdy += 1;
        return intArrayOf(luy, lux, rdy, rdx)
    }
}