function solution(s, skip, index) {
    var answer = '';
    let ascii_a = 'a'.charCodeAt(0);
    let ascii_z = 'z'.charCodeAt(0);
    let dics = [];
    const skips = skip.split('');
    
    for(let i = ascii_a; i <= ascii_z; i++) {
        dics.push(String.fromCharCode(i));
    }
    
    dics = dics.filter(item => !skips.includes(item));
    
    for(let c of s) {
        let idx = dics.indexOf(c);
        idx = (idx + index)%dics.length;
        answer += dics[idx];
    }
    

    return answer;
}