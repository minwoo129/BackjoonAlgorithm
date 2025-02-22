function solution(info, n, m) {
    const len = info.length;
    let minATrace = Infinity;
    
    const cache = new Map()
    
    const getCacheKey = (idx, aTrace, bTrace) => `${idx},${aTrace},${bTrace}`
    
    // DFS로 모든 가능한 조합을 탐색
    function dfs(index, aTrace, bTrace) {
        // 기저 조건: 모든 물건을 확인했을 때
        if (index === len) {
            // A와 B 모두 경찰에 붙잡히지 않는 경우에만 고려
            if (aTrace < n && bTrace < m) {
                minATrace = Math.min(minATrace, aTrace);
            }
            return;
        }
        
        const cacheKey = getCacheKey(index, aTrace, bTrace)
        if(cache.has(cacheKey)) {
            return
        }
        
        cache.set(cacheKey, true)
        
        // A가 물건을 훔치는 경우
        const newATrace = aTrace + info[index][0];
        if (newATrace < n) { // A가 경찰에 붙잡히지 않을 경우에만 진행
            dfs(index + 1, newATrace, bTrace);
        }
        
        // B가 물건을 훔치는 경우
        const newBTrace = bTrace + info[index][1];
        if (newBTrace < m) { // B가 경찰에 붙잡히지 않을 경우에만 진행
            dfs(index + 1, aTrace, newBTrace);
        }
    }
    
    // 초기 호출
    dfs(0, 0, 0);
    
    // 결과 반환
    return minATrace === Infinity ? -1 : minATrace;
}