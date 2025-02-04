class Solution {
    
    fun solution(weights: IntArray): Long {
        var answer: Long = 0
        var weightSets = mutableSetOf<Int>();
        var weightMaps = HashMap<Int, Long>();
        
        var ratio = arrayOf(2, 3, 4);
        var divider = arrayOf(1, 2, 3);
        
        for(w in weights) {
            weightSets.add(w);
            
            val cnt = weightMaps.getOrDefault(w, 0);
            weightMaps.put(w, (cnt+1).toLong());
        }
        
        for(weight in weightSets) {
            val weightCnt = weightMaps.getOrDefault(weight, 0);
            answer += (weightCnt * (weightCnt-1))/2
            for(i in 0 until 3) {
                if(weight % divider[i] > 0) {
                    continue;
                }
                
                val convertValue = (weight/divider[i]) * ratio[i];
                val convertCnt = weightMaps.getOrDefault(convertValue, 0)
                val cnt = (weightCnt*convertCnt)
                answer += cnt
            }
            
        }
        return answer
    }
}