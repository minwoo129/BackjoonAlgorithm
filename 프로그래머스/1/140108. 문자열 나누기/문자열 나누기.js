function solution(s) {
    var answer = 0;
    let checkCh = '';
    let checkChCount = 0;
    let nonCheckChCount = 0;
    
    for(let i = 0; i < s.length; i++) {
        const ch = s[i]
        if(checkCh === '') {
            checkCh = ch;
            checkChCount++;
            
            if(i === s.length-1) answer++
            continue;
        }
        
        if(checkCh === ch) checkChCount++;
        else nonCheckChCount++;
        
        if(checkChCount === nonCheckChCount || i === s.length-1) {
            answer++;
            checkCh = '';
            checkChCount = 0;
            nonCheckChCount = 0;
        }
    }
    
    return answer;
}