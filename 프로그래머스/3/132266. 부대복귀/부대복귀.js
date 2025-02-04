function solution(n, roads, sources, destination) {
    var answer = [];
    let graph = Array.from(Array(n+1), () => Array());
    let queue = [];
    let visited = Array.from({length: n+1}, () => Number.MAX_SAFE_INTEGER);
    
    for(let [a,b] of roads) {
        graph[a] = [ ...graph[a], b ];
        graph[b] = [ ...graph[b], a ]
    }
    
    queue.push(destination);
    visited[destination] = 0;
    while(queue.length != 0) {
        let point = queue.shift();
        for(let p of graph[point]) {
            if(visited[point]+1 < visited[p]) {
                visited[p] = visited[point]+1;
                queue.push(p)
            }
        }
    }
    
    return sources.map(idx => {
        if(visited[idx] == Number.MAX_SAFE_INTEGER) return -1;
        else return visited[idx]
    });
}