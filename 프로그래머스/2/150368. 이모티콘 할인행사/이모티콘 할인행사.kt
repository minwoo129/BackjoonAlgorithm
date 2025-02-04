import java.util.*

class Solution {
    fun solution(users: Array<IntArray>, emoticons: IntArray): IntArray {
        var answer: IntArray = intArrayOf()
        var rates = MutableList(emoticons.size) { 0 }
        var queue = PriorityQueue(compareByDescending<IntArray> { it[0] }.thenByDescending { it[1] })
        
        fun findSolution(): IntArray {
            val result = intArrayOf(0, 0)
            var count = 0;
            var sum = 0
            userLoop@ for(u in users) {
                var price = 0;
                for(i in emoticons.indices) {
                    if(rates[i] >= u[0]) {
                        price += emoticons[i] * (100-rates[i]) / 100
                        if(price >= u[1]) {
                            result[0]++;
                            count++;
                            continue@userLoop
                        }
                    }
                }
                result[1] += price
                sum += price
            }
            
            return intArrayOf(count, sum)
        }
        
        fun DFS(L: Int) {
            if(L == emoticons.size) {
                queue.offer(findSolution())
            }   
            else {
                for(i in 10..40 step (10)) {
                    rates[L] = i;
                    DFS(L+1);
                }
            }
        }
        
        DFS(0)

        return queue.peek()
    }
}