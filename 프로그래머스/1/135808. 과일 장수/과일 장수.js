function chunk(arr, size) {
    let newArr = [];
    
    for(let i = 0; i < arr.length; i += size) {
        newArr.push(arr.slice(i, i+size));
    }
    
    return newArr;
}

function solution(k, m, score) {
    var answer = 0;
    score.sort((a,b) => b-a);
    score = chunk(score, m);
    
    for(let arr of score) {
        if(arr.length === m) {
            const min = Math.min(...arr);
            answer += (min * m)
        }
    }
    
    return answer;
}