function solution(numbers, target) {
    var answer = 0;
    
    function DFS(l, sum) {
        if(l === numbers.length) {
            answer += (sum === target ? 1 : 0)
            return
        }
        
        DFS(l+1, sum + numbers[l])
        DFS(l+1, sum - numbers[l])
    }
    
    DFS(0, 0)
    return answer;
}