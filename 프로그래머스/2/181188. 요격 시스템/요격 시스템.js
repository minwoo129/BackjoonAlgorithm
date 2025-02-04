function solution(targets) {
    let answer = 0;
    targets.sort((a,b) => {
        if(a[1] == b[1]) {
            return a[0] - b[0];
        }
        return a[1] - b[1];
    })
    
    let cut = -1;
    for(let target of targets) {
        const left = target[0];
        const right = target[1];
        
        if(left >= cut) {
            answer++;
            cut = right
        }
    }
    
    return answer;
}