function solution(sequence, k) {
    var answer = [];
    let startIdx = 0;
    let result = [];
    let min = Number.MAX_SAFE_INTEGER
    let sum = 0;
    
    for(let i = 0; i < sequence.length; i++) {
        sum += sequence[i];
        if(sum > k) {
            while(sum > k) {
                sum -= sequence[startIdx++];
            }
        }
        if(sum === k) {
            answer.push([startIdx, i])
        }
        
    }
    answer.forEach(item => {
        if(min > (item[1] - item[0])) {
            min = item[1] - item[0];
            result = [item[0], item[1]]
        }
    })
    
    
    return result;
}