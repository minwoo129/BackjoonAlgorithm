function solution(sales, links) {
    const n = sales.length
    const tree = Array.from({length: n+1}, () => [])
    const dp = Array.from({length: n+1}, () => [0, 0])
    
    for(const [leader, member] of links) {
        tree[leader].push(member)
    }
    
    function dfs(node) {
        if(tree[node].length === 0) {
            dp[node][0] = 0
            dp[node][1] = sales[node-1]
            return
        }
        
        let sum = 0
        let minDiff = Infinity
        let hasSelected = false
        
        for(const child of tree[node]) {
            dfs(child)
            sum += Math.min(dp[child][0], dp[child][1])
            
            if(dp[child][1] <= dp[child][0]) {
                hasSelected = true
            }
            
            minDiff = Math.min(minDiff, dp[child][1] - dp[child][0])
        }
        
        dp[node][0] = sum + (hasSelected ? 0 : minDiff)
        
        dp[node][1] = sum + sales[node-1]
    }
    
    dfs(1)
    return Math.min(dp[1][0], dp[1][1])
}