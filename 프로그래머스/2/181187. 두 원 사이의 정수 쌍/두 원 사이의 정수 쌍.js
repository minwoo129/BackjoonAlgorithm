// function solution(r1, r2) {
//     var answer = 0;
//     const min = r1 ** 2;
//     const max = r2 ** 2;
    
//     for(let x = 1; x < r2; x++) {
//         for(let y = 1; y < r2; y++) {
//             let pointSum = (x**2) + (y**2);
            
//             if((pointSum >= min) && (pointSum <= max)) answer++;
//         }
//     }
//     answer += (r2-r1+1);
    
//     answer *= 4;
    
//     return answer;
// }
function getHeight(r, x) {
    let height = (r ** 2) - (x ** 2);
    height = Math.sqrt(height);
    return Math.floor(height);
}
function solution(r1, r2) {
    var answer = 0;
    
    for(let x = 1; x <= r2; x++) {
        const maxY = Math.floor(Math.sqrt(r2 ** 2 - x ** 2))
        let minY = 0
        if(x < r1) {
            minY = Math.ceil(Math.sqrt(r1 ** 2 - x ** 2))
        }
        answer += (maxY-minY+1)
    }
    
    answer *= 4;
    
    return answer;
}

