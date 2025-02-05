function solution(my_string, n) {
    var answer = '';
    
    for(let ch of my_string) {
        answer += ch.repeat(n)
    }
    return answer;
}