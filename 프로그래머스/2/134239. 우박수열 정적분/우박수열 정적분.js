function solution(k, ranges) {
    var answer = [];
    let parts = [];
    while(k != 1) {
        parts.push(k);
        if(k%2 == 0) {
            k /= 2;
        }
        else {
            k *= 3;
            k += 1;
        }
    }
    parts.push(1);
    let len = parts.length;
    
    for(let [start, limit] of ranges) {
        let res = 0;
        
        if(start >= len+limit) {
            answer.push(-1);
            continue;
        }
        
        for(let j = start; j < len+limit-1; j++) {
            res += (parts[j] + parts[j+1])/2
        }
        answer.push(res)
    }
    return answer;
}