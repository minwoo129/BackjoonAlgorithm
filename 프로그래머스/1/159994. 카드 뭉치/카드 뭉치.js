function solution(cards1, cards2, goal) {
    var answer = 'Yes';
    
    for(let str of goal) {
        if(cards1[0] && cards1[0] === str) {
            cards1.shift();
        }
        else if(cards2[0] && cards2[0] === str) {
            cards2.shift()
        }
        else {
            answer = 'No';
            break;
        }
    }
    return answer;
}