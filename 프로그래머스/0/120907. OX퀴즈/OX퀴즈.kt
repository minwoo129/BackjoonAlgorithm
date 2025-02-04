class Solution {
    fun solution(quiz: Array<String>): Array<String> {
        var answer: Array<String> = arrayOf<String>()
        
        for(q in quiz) {
            var arr1 = q.split(" = ").toTypedArray();
            var z = arr1[1].toString().toInt();
            var arr2 = arr1[0].split(" ").toTypedArray();
            var x = arr2[0].toString().toInt();
            var type = arr2[1].toString();
            var y = arr2[2].toString().toInt();
            
            var result:Int = 0;
            
            if(type == "+") {
                result = x+y;
            }
            else {
                result = x-y;
            }
            
            if(result == z) answer += "O";
            else answer += "X";
            
        }
        return answer
    }
}