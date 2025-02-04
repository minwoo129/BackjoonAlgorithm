function solution(s) {
    let answer = [];
    let charArr = Array.from(new Set(s.split('')));
    let chars = {};
    
    for(let ch of charArr) chars[ch] = -1;
    
    for(let i = 0; i < s.length; i++) {
        const ch = s[i];
        const beforeIdx = chars[ch];
        
        if(beforeIdx === -1) {
            answer.push(-1);
            chars[ch] = i;
        }
        else {
            answer.push(i-beforeIdx);
            chars[ch] = i;
        }
    } 
    return answer;
}