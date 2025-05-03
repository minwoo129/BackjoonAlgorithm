function solution(maze) {
  const n = maze.length;
  const m = maze[0].length;
  const N = n * m;

  // Directions: up, down, left, right
  const dirs = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];

  // Map 2D coords to single index 0..N-1
  const idx = (r, c) => r * m + c;

  let redStart, blueStart, redDest, blueDest;
  const isWall = new Array(N).fill(false);

  // Locate starts, dests, walls
  for (let r = 0; r < n; r++) {
    for (let c = 0; c < m; c++) {
      const v = maze[r][c];
      const id = idx(r, c);
      if (v === 1) redStart = id;
      else if (v === 2) blueStart = id;
      else if (v === 3) redDest = id;
      else if (v === 4) blueDest = id;
      else if (v === 5) isWall[id] = true;
    }
  }

  // Early impossible: one cart already on other's dest or start overlap
  if (redStart === blueStart || redStart === blueDest ||
      blueStart === redDest || redDest === blueDest) {
    return 0;
  }

  // BFS state: [redPos, bluePos, redVisitedMask, blueVisitedMask, steps]
  const queue = [];
  let head = 0;

  const initRVisited = 1 << redStart;
  const initBVisited = 1 << blueStart;

  queue.push([redStart, blueStart, initRVisited, initBVisited, 0]);

  // Track visited states to avoid repeats
  const seen = new Set();
  seen.add(`${redStart},${blueStart},${initRVisited},${initBVisited}`);

  while (head < queue.length) {
    const [rPos, bPos, rVis, bVis, steps] = queue[head++];
    // If both at their destinations, we're done
    if (rPos === redDest && bPos === blueDest) {
      return steps;
    }

    // Generate all pairs of moves (dr, dc) for each cart
    for (const [dr1, dc1] of dirs) {
      // compute new red position (or stay if already at dest)
      let newR = rPos;
      if (rPos !== redDest) {
        const rr = Math.floor(rPos / m) + dr1;
        const rc = (rPos % m) + dc1;
        if (
          rr < 0 || rr >= n ||
          rc < 0 || rc >= m
        ) continue; // out of bounds
        const nid = idx(rr, rc);
        if (
          isWall[nid] ||               // wall
          (rVis & (1 << nid)) !== 0    // already visited
        ) continue;
        newR = nid;
      }

      for (const [dr2, dc2] of dirs) {
        // compute new blue position (or stay if already at dest)
        let newB = bPos;
        if (bPos !== blueDest) {
          const br = Math.floor(bPos / m) + dr2;
          const bc = (bPos % m) + dc2;
          if (
            br < 0 || br >= n ||
            bc < 0 || bc >= m
          ) continue; // out of bounds
          const bid = idx(br, bc);
          if (
            isWall[bid] ||               // wall
            (bVis & (1 << bid)) !== 0    // already visited
          ) continue;
          newB = bid;
        }

        // Cannot collide
        if (newR === newB) continue;
        // Cannot swap places in one move
        if (newR === bPos && newB === rPos) continue;

        // Update visited masks
        const newRVis = rVis | (1 << newR);
        const newBVis = bVis | (1 << newB);

        const key = `${newR},${newB},${newRVis},${newBVis}`;
        if (seen.has(key)) continue;
        seen.add(key);
        queue.push([newR, newB, newRVis, newBVis, steps + 1]);
      }
    }
  }

  // No solution found
  return 0;
}