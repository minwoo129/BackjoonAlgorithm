function solution(rsp) {
    var answer = '';
    
    // 0: 묵, 2: 찌, 5: 빠
    let rspMap = {
        '0': '5',
        '2': '0',
        '5': '2'
    }
    
    for(const ch of rsp) {
        answer += rspMap[ch]
    }
    return answer;
}