import java.util.*

class Solution {
    fun solution(x: Int, y: Int, n: Int): Int {
        var answer: Int = 0
        var queue: Queue<PointCount> = LinkedList();
        var answers = mutableListOf<Int>();
        var visited: HashMap<Int, Boolean> = hashMapOf();
        
        queue.add(PointCount(x, 0));
        
        while(queue.isNotEmpty()) {
            val cur = queue.poll();
            val point = cur.point;
            val cnt = cur.cnt;
            
            if(point > y) continue;
            if(point == y) {
                answers.add(cnt);
                break
            }
            
            if(!(visited[point+n] ?: false)) {
                queue.add(PointCount(point+n, cnt+1));
                visited[point+n] = true
            }
            if(!(visited[point*2] ?: false)) {
                queue.add(PointCount(point*2, cnt+1));
                visited[point*2] = true
            }
            if(!(visited[point*3] ?: false)) {
                queue.add(PointCount(point*3, cnt+1));
                visited[point*3] = true
            }
            
        }
        
        if(answers.isEmpty()) return -1;
        else return answers.first()
    }
    
    data class PointCount(
        val point: Int,
        val cnt: Int
    )
}