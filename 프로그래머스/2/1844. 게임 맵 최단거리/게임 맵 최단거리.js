function solution(maps) {
    var answer = 1;
    let visited = maps
    const dx = [0, 1, 0, -1];
    const dy = [1, 0, -1, 0];
    const n = maps.length, m = maps[0].length;
    let queue = []
    
    queue.push([0, 0])
    visited[0][0] = 0
    
    while(queue.length != 0) {
        const size = queue.length
        for(let i = 0; i < size; i++) {
            const [x, y] = queue.shift();
            for(let j = 0; j < 4; j++) {
                const nx = x + dx[j]
                const ny = y + dy[j];

                if((nx >= 0 && nx < n)&&(ny >= 0 && ny < m)&&(visited[nx][ny] === 1)) {
                    if((nx === n-1)&&(ny === m-1)) {
                        return ++answer
                    }
                    queue.push([nx, ny])
                    visited[nx][ny] = 0
                }
            }
        }
        answer++
    }
    return -1;
}