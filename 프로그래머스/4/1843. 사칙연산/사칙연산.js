function solution(arr) {
    const m = arr.length;
    const n = (m+1) / 2
    const nums = Array(n)
    const ops = Array(n-1)
    
    let numIdx = 0, opsIdx = 0
    
    for(let i = 0; i < m; i++) {
        if(i % 2 === 0) {
            nums[numIdx++] = parseInt(arr[i], 10)
        }
        else {
            ops[opsIdx++] = arr[i]
        }
    }
    
    const dpMax = Array.from({length: n}, () => Array(n).fill(Number.MIN_SAFE_INTEGER))
    const dpMin = Array.from({length: n}, () => Array(n).fill(Number.MAX_SAFE_INTEGER))
    
    for(let i = 0; i < n; i++) {
        dpMax[i][i] = dpMin[i][i] = nums[i]
    }
    
    for(let len = 2; len <= n; len++) {
        for(let i = 0; i + len - 1 < n; i++) {
            const j = i + len - 1
            for(let k = i; k < j; k++) {
                const op = ops[k]
                if(op === '+') {
                    dpMax[i][j] = Math.max(dpMax[i][j], dpMax[i][k] + dpMax[k+1][j])
                    dpMin[i][j] = Math.min(dpMin[i][j], dpMin[i][k] + dpMin[k+1][j])
                }
                else {
                    dpMax[i][j] = Math.max(dpMax[i][j], dpMax[i][k] - dpMin[k+1][j])
                    dpMin[i][j] = Math.min(dpMin[i][j], dpMin[i][k] - dpMax[k+1][j])
                }
            }
        }
    }
    
    return dpMax[0][n-1]
}