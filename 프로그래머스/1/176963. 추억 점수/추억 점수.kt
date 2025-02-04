class Solution {
    fun solution(name: Array<String>, yearning: IntArray, photo: Array<Array<String>>): IntArray {
        var answer: IntArray = intArrayOf()
        val yearnMap = HashMap<String,Int>();
        
        for(i in 0..name.size-1) {
            yearnMap.put(name[i], yearning[i]);
        }
        
        for(p in photo) {
            answer += calculateYearn(yearnMap, p);
        }
        
        return answer
    }
    
    fun calculateYearn(yearnMap: HashMap<String,Int>, photos: Array<String>) : Int {
        var yearn:Int = 0;
        
        for(photo in photos) {
            yearn += yearnMap.getOrDefault(photo, 0);
        }
        return yearn;
    }
}