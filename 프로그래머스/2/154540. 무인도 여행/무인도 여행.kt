class Solution {
    fun solution(maps: Array<String>): IntArray {
        var answer: IntArray = intArrayOf()
        var width = maps[0].length;
        var height = maps.size;
        var convertedMap = mutableListOf<MutableList<Char>>();
        
        for(str in maps) {
            var newArr = mutableListOf<Char>();
            for(ch in str) {
                newArr.add(ch);
            }
            convertedMap.add(newArr);
        }
        
        for(i in 0 until height) {
            for(j in 0 until width) {
                if(convertedMap[i][j] == 'X') continue;
                
                var queue = mutableListOf<Point>(Point(i, j));
                var sum = 0;
                while(queue.isNotEmpty()) {
                    val p = queue.removeAt(0);
                    var (y, x) = p;
                    var v = convertedMap[y][x];
                    
                    if(v == 'X') continue;
                    
                    sum += v.toString().toInt();

                    convertedMap[y][x] = 'X';
                    val dx = arrayOf(0, 1, 0, -1);
                    val dy = arrayOf(-1, 0, 1, 0);
                    
                    for(k in 0 until 4) {
                        val nx = x + dx[k];
                        val ny = y + dy[k];
                        
                        if((nx >= 0)&&(nx < width)&&(ny >= 0)&&(ny < height)&&(convertedMap[ny][nx] != 'X')) {
                            queue.add(Point(ny, nx));
                        }
                        
                    }
                }
                
                answer += sum;
            }
        }
        
        if(answer.size == 0) answer += -1;
        
        answer.sort()

        return answer
    }
    
    data class Point(val y:Int, val x:Int);
}