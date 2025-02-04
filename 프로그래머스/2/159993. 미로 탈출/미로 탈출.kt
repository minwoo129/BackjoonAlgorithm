class Solution {
    fun solution(maps: Array<String>): Int {
        var answer: Int = -1;
        var start = Point(0, 0);
        var end = Point(0, 0);
        var lever = Point(0, 0);
        
        for(i in 0 until maps.size) {
            val str = maps[i];
            for(j in 0 until str.length) {
                if(str[j] == 'S') start = Point(i, j);
                else if(str[j] == 'E') end = Point(i, j);
                else if(str[j] == 'L') lever = Point(i, j);
            }
        }
        
        val startToLever = findMinDistance(start, lever, maps);
        if(startToLever == 0) return -1;
        val leverToEnd = findMinDistance(lever, end, maps);
        if(leverToEnd == 0) return -1;
        
        return (startToLever+leverToEnd)
    }
    
    fun findMinDistance(start: Point, end: Point, maps: Array<String>): Int {
        var queue = mutableListOf<Point>(start);
        var counts: MutableList<MutableList<Int>> = mutableListOf();
        for(str in maps) {
            var arr = mutableListOf<Int>();
            for(ch in str) {
                if(ch == 'X') arr.add(-1);
                else arr.add(0);
            }
            counts.add(arr);
        }
        
        var width = maps[0].length;
        var height = maps.size;
        
        while(queue.isNotEmpty()) {
            var curLoc = queue.removeAt(0);
            var (y, x) = curLoc;
            var curCnt = counts[y][x];
            var nextCnt = curCnt+1;
            
            val dx = intArrayOf(0, 1, 0, -1);
            val dy = intArrayOf(-1, 0, 1, 0);
            
            for(i in 0 until 4) {
                val nx = x + dx[i];
                val ny = y + dy[i];
                
                if((nx >= 0)&&(nx < width)&&(ny >= 0)&&(ny < height)&&(counts[ny][nx] == 0)) {
                    queue.add(Point(ny, nx));
                    counts[ny][nx] = nextCnt;
                }
            }
        }
        
        return counts[end.y][end.x];
    }
    
    data class Point(val y: Int, val x: Int);
}