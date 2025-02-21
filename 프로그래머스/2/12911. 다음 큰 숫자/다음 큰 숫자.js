function solution(n) {
    var answer = 0;
    
    const cnt_1 = n.toString(2).split("").reduce((acc, cur) => acc + (cur === "1" ? 1 : 0), 0)
    
    while(n <= 1000000) {
        n++
        const cnt = n.toString(2).split("").reduce((acc, cur) => acc + (cur === "1" ? 1: 0), 0)
        if(cnt_1 === cnt) {
            return n
        }

    }
    return n;
}