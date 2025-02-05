class Solution {
    fun solution(polynomial: String): String {
        var answer: String = ""
        var pc:Int = 0;
        var pcType:String = "";
        var cons:Int = 0;
        
        var polyList = polynomial.split(" ").toList();
        
        for(item in polyList) {
            var num:Int = 0;
            if(item.contains("x")) {
                if(item == "x") num = 1;
                else {
                    num = item.replace("x".toRegex(), "").toInt()
                }
                
                pc += num;
            }
            else if(item != "+") {
                num = item.toInt();
                
                cons += num;
            }
        }
        
        
        if(pc != 0 && cons != 0) {
            if(pc > 1) answer = "${pc}x + ${cons}"
            else answer = "x + ${cons}";
        };
        else if(pc != 0 && cons == 0) {
            if(pc > 1) answer = "${pc}x"
            else answer = "x"
        }
        else if(pc == 0 && cons != 0) answer = "${cons}"
        
        return answer
    }
}