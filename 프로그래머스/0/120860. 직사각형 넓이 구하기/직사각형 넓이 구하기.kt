class Solution {
    fun solution(dots: Array<IntArray>): Int {
        var answer: Int = 0
        var setX = HashSet<Int>()
        var setY = HashSet<Int>();
        
        for(dot in dots) {
            setX.add(dot[0]);
            setY.add(dot[1]);
        }
        
        var arrayX = ArrayList(setX);
        var arrayY = ArrayList(setY);
        
        answer = Math.abs(arrayX[0]-arrayX[1]) * Math.abs(arrayY[0] - arrayY[1])
        return answer
    }
}