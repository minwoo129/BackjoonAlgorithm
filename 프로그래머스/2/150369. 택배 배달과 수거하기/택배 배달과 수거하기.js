function solution(cap, n, deliveries, pickups) {
    var answer = 0;
    
    while(deliveries.length || pickups.length) {
        let w = cap;
        let dis1 = 0, dis2 = 0;
        for(let i = deliveries.length-1; i >= 0; i--) {
            if(deliveries[i] !== 0) {
                if(w === cap) dis1 = i+1;
                if(deliveries[i] <= w) {
                    w -= deliveries[i];
                    deliveries.pop();
                }
                else {
                    deliveries[i] -= w;
                    break;
                }
            }
            else deliveries.pop() 
        }
        w = cap;
        for(let i = pickups.length-1; i >= 0; i--) {
            if(pickups[i] !== 0) {
                if(w === cap) dis2 = i+1
                if(pickups[i] <= w) {
                    w -= pickups[i];
                    pickups.pop();
                }
                else {
                    pickups[i] -= w;
                    break
                }
            }
            else pickups.pop();
        }
        
        answer += Math.max(dis1, dis2)*2
    }
    
    return answer;
}