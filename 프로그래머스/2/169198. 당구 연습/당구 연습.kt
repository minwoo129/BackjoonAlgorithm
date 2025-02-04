class Solution {
    fun solution(m: Int, n: Int, startX: Int, startY: Int, balls: Array<IntArray>): IntArray {
        var answer: IntArray = intArrayOf()
        var width = m.toDouble();
        var height = n.toDouble();
        var p = 2.0;
        
        for(ball in balls) {
            var targetX = ball[0];
            var targetY = ball[1];
            var sX = startX.toDouble();
            var sY = startY.toDouble()
            var tX = targetX.toDouble();
            var tY = targetY.toDouble();
            var minValue = Integer.MAX_VALUE;
            
            var up = Math.pow(sX-tX, p).toInt() + Math.pow(height*2.0 - sY - tY, p).toInt()
            var down = Math.pow(sX-tX, p).toInt() + Math.pow(sY+tY, p).toInt();
            var left = Math.pow(sX+tX, p).toInt() + Math.pow(sY-tY, p).toInt();
            var right = Math.pow(width*2.0 - sX - tX, p).toInt() + Math.pow(sY-tY, p).toInt();
            
            var list = mutableListOf<Int>()
            list.add(up);
            list.add(down);
            list.add(left);
            list.add(right);
            
            if(startX == targetX && targetY > startY) {
                list.removeAt(0);
            }
            else if(startX == targetX && targetY < startY) {
                list.removeAt(1);
            }
            else if(startY == targetY && targetX < startX) {
                list.removeAt(2)
            }
            else if(startY == targetY && targetX > startX) {
                list.removeAt(3);
            }
            
            for(item in list) {
                if(minValue > item) minValue = item
            }
            
            answer += minValue
            
        }
        return answer
    }
}