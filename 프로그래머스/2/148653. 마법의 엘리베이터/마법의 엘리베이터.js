function solution(storey) {
    let answer = 0;
    let split = String(storey).split('').map(n => parseInt(n));
    
    for(let i = split.length-1; i >= 0; i--) {
        if(split[i] > 5) {
            answer += (10-split[i]);
            if(i == 0) answer++
            split[i-1]++;
        }
        else if(split[i] === 5 && split[i-1] >= 5) {
            answer += 5;
            split[i-1]++;
        }
        else answer += split[i]
        
    }
    
    return answer;
}