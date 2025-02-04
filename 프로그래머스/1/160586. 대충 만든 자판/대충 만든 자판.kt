class Solution {
    fun solution(keymap: Array<String>, targets: Array<String>): IntArray {
        var answer: IntArray = intArrayOf()
        var keys = HashMap<Char, Int>();
        var joined = keymap.joinToString("")
        var keySet = mutableSetOf<Char>();
        
        
        for(s in joined) {
            keySet.add(s);
        }
        
        for(s in keySet) {
            
            var idxs = intArrayOf();
            for(s1 in keymap) {
                var idx = s1.indexOf(s);
                if(idx != -1) idxs += (idx+1);
            }
            keys.put(s, idxs.minOrNull() ?: 0);
        }
        
        for(target in targets) {
            var targetKeys = target.toCharArray();
            var count = 0;
            for(t in targetKeys) {
                if(keys.containsKey(t)) {
                    count += keys.getOrDefault(t, 0);
                }
                else {
                    count = -1;
                    break;
                }
            }
            
            answer += count;
        }
        return answer
    }
}