function solution(edges, target) {
  const n = target.length;
  // Build children lists
  const children = Array.from({length: n+1}, () => []);
  for (const [u,v] of edges) {
    children[u].push(v);
  }
  for (let u = 1; u <= n; u++) {
    children[u].sort((a,b)=>a-b);
  }
  // Identify leaves
  const isLeaf = Array(n+1).fill(false);
  for (let u = 1; u <= n; u++) {
    if (children[u].length === 0) isLeaf[u] = true;
  }
  const leaves = [];
  for (let u = 1; u <= n; u++) {
    if (isLeaf[u]) leaves.push(u);
  }
  // total sum we need to drop
  const sumTarget = target.reduce((a,b)=>a+b, 0);
  // min drops m must satisfy 3m >= sumTarget => m >= ceil(sumTarget/3)
  const mMin = Math.ceil(sumTarget/3);
  
  // pointers[u] = index into children[u] of the "current" outgoing edge
  const pointers = Array(n+1).fill(0);
  for (let u = 1; u <= n; u++) {
    if (children[u].length > 1) pointers[u] = 0;
    // if 0 or 1 child, pointer[u] stays 0
  }
  
  // Track how many times each leaf has been visited in the first j drops
  const visitCount = Array(n+1).fill(0);
  // sequence of leaf hits for j=0,1,...
  const seq = [];
  
  let m = -1;
  const ceil3 = x => Math.ceil(x/3);
  
  // simulate drop by drop
  for (let j = 0; j < sumTarget; j++) {
    // follow pointers from root=1 to a leaf
    let u = 1;
    const path = [];  // nodes on the path (for pointer-updates)
    while (children[u].length > 0) {
      path.push(u);
      const idx = pointers[u];
      u = children[u][idx];
    }
    // u is now a leaf
    seq.push(u);
    visitCount[u]++;
    // if we ever visit a leaf more than its target, impossible
    if (visitCount[u] > target[u-1]) {
      return [-1];
    }
    // check if we can stop here
    const used = j+1;
    if (used >= mMin) {
      let ok = true;
      for (const ℓ of leaves) {
        const v = visitCount[ℓ];
        const T = target[ℓ-1];
        // must have enough visits to reach T but not too many
        if (v < ceil3(T) || v > T) {
          ok = false;
          break;
        }
      }
      if (ok) {
        m = used;
        break;
      }
    }
    // advance each pointer along the path
    for (const x of path) {
      const c = children[x];
      if (c.length <= 1) {
        pointers[x] = 0;
      } else {
        pointers[x] = (pointers[x] + 1) % c.length;
      }
    }
  }
  if (m < 0) {
    // never found a valid stop
    return [-1];
  }
  
  // Now we have seq[0..m-1], visitCount[ℓ] for each leaf ℓ.
  // Greedily assign k[j] ∈ {1,2,3}, lexicographically smallest
  const k = Array(m).fill(0);
  // remaining visits per leaf
  const remVisits = Array(n+1).fill(0);
  for (let j = 0; j < m; j++) {
    remVisits[ seq[j] ]++;
  }
  // remaining sum to assign per leaf
  const remSum = target.slice(); // remSum[ℓ-1]
  
  for (let j = 0; j < m; j++) {
    const ℓ = seq[j];
    const idx = ℓ - 1;
    // for this position try k = 1,2,3
    for (let cand = 1; cand <= 3; cand++) {
      if (cand > remSum[idx]) break;
      const newSum = remSum[idx] - cand;
      const newVisits = remVisits[ℓ] - 1;
      // can the remaining newVisits achieve newSum?
      if (newVisits >= ceil3(newSum) && newVisits <= newSum) {
        k[j] = cand;
        remSum[idx] = newSum;
        remVisits[ℓ] = newVisits;
        break;
      }
    }
  }
  
  return k;
}