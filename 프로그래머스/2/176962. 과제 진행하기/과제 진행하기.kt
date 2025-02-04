class Solution {
    fun solution(plans: Array<Array<String>>): Array<String> {
        var answer: Array<String> = arrayOf<String>()
        var plansList = MutableList(plans.size, { i -> plans[i].toMutableList() })
        var leftTimes = HashMap<String,Int>();
        var stack = mutableListOf<String>();
        
        plansList.sortBy { it[1] }
        
        for(plan in plansList) {
            leftTimes.put(plan[0], plan[2].toInt())
        }
        
        for(i in 0 until plansList.size) { 
            var plan = plansList[i];
            
            var curTime = convertTime(plan[1])
            var curLeftTime = plan[2].toInt();
            
            if(i != plansList.size-1) {
                var nextPlan = plansList[i+1];
                var nextTime = convertTime(nextPlan[1]);
                var nextLeftTime = nextPlan[2].toInt();
                
                if(curTime + curLeftTime <= nextTime) {
                    leftTimes.put(plan[0], 0);
                    answer += plan[0]
                    var left = nextTime - (curTime + curLeftTime);
                    while(left > 0 && !stack.isEmpty()) {
                        var sub = stack.removeLast();
                        var time = leftTimes.getOrDefault(sub, 0);
                        
                        if(left-time >= 0) {
                            left -= time;
                            leftTimes.put(sub, 0);
                            answer += sub;
                        }
                        else {
                            stack.add(sub);
                            leftTimes.put(sub, time-left);
                            left = 0;
                        }
                    }
                }
                else {
                    stack.add(plan[0]);
                    leftTimes.put(plan[0], (curTime+curLeftTime)-nextTime);
                }
            }
            else {
                answer += plan[0];
                leftTimes.put(plan[0], 0)
            }
            
        }
        
        while(stack.size > 0) {
            answer += stack.removeLast();
        }
        
        return answer
    }
    
    fun convertTime(time: String): Int {
        var arr = time.split(":");
        
        var hour = arr[0].toInt();
        var min = arr[1].toInt();
        
        return ((hour*60) + min);
    }
    
}