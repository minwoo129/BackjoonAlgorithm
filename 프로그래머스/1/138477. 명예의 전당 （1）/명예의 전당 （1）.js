function solution(k, score) {
    var answer = [];
    let arr = [];
    
    for(let s of score) {
        if(arr.length <= k) arr.push(s);
        arr.sort((a,b) => a-b);
        
        if(arr.length <= k) answer.push(arr[0]);
        else {
            arr = arr.slice(1);
            answer.push(arr[0]);
        }
        
    }
    return answer;
}