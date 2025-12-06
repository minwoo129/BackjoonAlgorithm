function solution(n, w, num) {
    var answer = 0;
    const r = Math.ceil(n/w)
    
    let isRight = true
    let targetPoint = -1
    let point = 0
    
    for(let i = 1; i <= n; i++) {
        if(i === num) {
            targetPoint = point
        }
        
        if(point === targetPoint) {
            answer++
        }
        
        if(isRight) {
            if(point === w-1) {
                isRight = false
            }
            else {
                point++
            }
        }
        else {
            if(point === 0) {
                isRight = true
            }
            else {
                point--
            }
        }
    }
    
    return answer;
}