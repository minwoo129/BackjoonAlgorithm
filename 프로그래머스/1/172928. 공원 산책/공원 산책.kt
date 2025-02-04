class Solution {
    fun solution(park: Array<String>, routes: Array<String>): IntArray {
        var answer: IntArray = intArrayOf()
        var map = Array(park.size, {i -> park[i].toCharArray()})
        
        var isBreak = false;
        for(i in 0..map.size-1) {
            for(j in 0..map[i].size-1) {
                if(map[i][j] == 'S') {
                    answer += i;
                    answer += j;
                    isBreak = true;
                    break
                }
            }
            
            if(isBreak) break;
        }
        
        for(route in routes) {
            answer = move(map, answer, route)
        }
        return answer
    }
    
    fun move(map: Array<CharArray>, pos: IntArray, route: String): IntArray {
        val w = map[0].size;
        val h = map.size;
        
        var current = intArrayOf(pos[0], pos[1])
        val dx = intArrayOf(0, 1, 0, -1);
        val dy = intArrayOf(-1, 0, 1, 0);
        val dirs = arrayOf("N", "E", "S", "W");
        
        var routeArr = route.split(" ").toTypedArray();
        val dir = routeArr[0]
        val moveCnt = routeArr[1].toInt();
        val idx = dirs.indexOf(dir);
        
        for(i in 0..moveCnt-1) {
            var currX = current[1] + dx[idx];
            var currY = current[0] + dy[idx];
            
            if(currX < 0 || currX >= w || currY < 0 || currY >= h || map[currY][currX] == 'X') {
                current = pos;
                break;
            }
            else {
                current[0] = currY;
                current[1] = currX;
            }
        }
        
        return current;
        
    }
}