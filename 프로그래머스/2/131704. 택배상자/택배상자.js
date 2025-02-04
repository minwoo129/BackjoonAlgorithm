function solution(order) {
    var answer = 0;
    let stack = [];
    let n = order.length;
    let idx = 0;
    for(let i = 1; i<= n; i++) {
        stack.push(i);
        while(stack[stack.length-1] == order[idx] && stack.length > 0) {
            stack.pop();
            answer++;
            idx++;
        }
    }
    return answer;
}