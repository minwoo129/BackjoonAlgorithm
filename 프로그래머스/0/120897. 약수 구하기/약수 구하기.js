function solution(n) {
    let answer = [];
    answer.push(1);
    for(let i = 2; i <= n; i++) {
        if(n%i === 0) answer.push(i);
    }
    return answer;
}