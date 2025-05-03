function solution(n, tops) {
    const MOD = 10007
//     var answer = 0;
//     let dp = Array(n+1).fill().map(() => [0, 0])
    
//     dp[0] = [1, 1]
    
//     for(let i = 1; i <= n; i++) {
//         const prev = dp[i-1]
//         const hasTop = tops[i-1]
        
//         if(hasTop) {
//             dp[i][0] = ((prev[0] + prev[1])*3) % MOD
//             dp[i][1] = ((prev[0] + prev[1])*2) % MOD
//         }
//         else {
//             dp[i][0] = ((prev[0] + prev[1])*2) % MOD
//             dp[i][1] = ((prev[0] + prev[1])*1) % MOD
//         }
//     }
//     return (dp[n][0] + dp[n][1]) % MOD;
    const f = new Array(2 * n + 2)
    
    f[2*n] = 1
    f[2*n+1] = 1
    
    for(let j = 2*n-1; j >= 0; --j) {
        let extra = 0
        if(j % 2=== 1) {
            const i = (j-1 >> 1)
            if(tops[i] === 1) extra = 1
            
        }
        
        f[j] = (f[j+1] * (1 + extra) + f[j+2]) % MOD
    }
    
    return f[0]
}