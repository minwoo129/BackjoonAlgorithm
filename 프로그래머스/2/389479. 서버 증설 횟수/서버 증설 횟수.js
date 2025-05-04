function solution(players, m, k) {
    var answer = 0;
    let ends = []
    let curServerCnt = 0
    
    for(let i = 0; i < players.length; i++) {
        const user = players[i]
        
        if(ends.length > 0) {
            const {end, decCnt} = ends[0]
            
            if(i === end) {
                ends.shift()
                curServerCnt -= decCnt
            }
        }
        
            
        if(user === 0) {
            continue
        }
        
        const reqServer = Math.floor(user / m)
        
        if(reqServer <= curServerCnt) {
            continue
        }
        
        const added = (reqServer - curServerCnt)

        ends.push({end: i+k, decCnt: added})
        answer += added
        curServerCnt = reqServer
        
        
    }
    
    return answer;
}