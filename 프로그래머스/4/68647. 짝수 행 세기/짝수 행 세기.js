function solution(a) {
  const mod = 10000019;
  const N = a.length;
  const M = a[0].length;
  
  // 1) 각 열의 1 개수 c_j 계산
  const c = Array(M).fill(0);
  let totalOnes = 0;
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      c[j] += a[i][j];
      totalOnes += a[i][j];
    }
  }
  // 행마다 짝수 개의 1을 가져야 하므로, 전체 1의 개수는 짝수여야 한다
  if (totalOnes % 2 !== 0) return 0;
  
  // 2) 팩토리얼과 역팩토리얼 미리 계산 (0..N)
  const fac = Array(N+1).fill(1);
  for (let i = 1; i <= N; i++) fac[i] = fac[i-1] * i % mod;
  const invfac = Array(N+1);
  invfac[N] = modPow(fac[N], mod-2, mod);
  for (let i = N; i >= 1; i--) {
    invfac[i-1] = invfac[i] * i % mod;
  }
  // 조합 함수
  const nCr = (n, r) => {
    if (r < 0 || r > n) return 0;
    return fac[n] * invfac[r] % mod * invfac[n-r] % mod;
  };
  
  // 3) 각 열 j에 대해, k(0..N)별로 Krawtchouk 다항식 P_{c_j}(k) 계산
  //    P_c(k) = sum_{i=0..c} (-1)^i * C(k,i) * C(N-k, c-i)
  const P = Array(M);
  for (let j = 0; j < M; j++) {
    const cj = c[j];
    const Pj = Array(N+1).fill(0);
    for (let k = 0; k <= N; k++) {
      let v = 0;
      // i 범위: i = 0..cj 이지만 C(...)가 0이 되는 부분은 건너뛰기
      const iMin = Math.max(0, cj - (N - k));
      const iMax = Math.min(cj, k);
      for (let i = iMin; i <= iMax; i++) {
        const sign = (i & 1) ? mod - 1 : 1;
        const term = nCr(k, i) * nCr(N - k, cj - i) % mod;
        v = (v + sign * term) % mod;
      }
      Pj[k] = v;
    }
    P[j] = Pj;
  }
  
  // 4) k=0..N 에 대해 Mprod_k = ∏_{j=1..M} P_j[k]
  //    그리고 sum += C(N,k) * Mprod_k
  let sum = 0;
  for (let k = 0; k <= N; k++) {
    let prod = 1;
    for (let j = 0; j < M; j++) {
      prod = prod * P[j][k] % mod;
      if (prod === 0) break;
    }
    if (prod !== 0) {
      sum = (sum + prod * nCr(N, k)) % mod;
    }
  }
  
  // 5) 결과 = sum / 2^N  (mod 역원 곱)
  //    mod는 홀수이므로 2의 역원 inv2 = (mod+1)/2
  const inv2 = (mod + 1) >> 1;
  const inv2N = modPow(inv2, N, mod);
  
  return sum * inv2N % mod;
}

/** 
 * 빠른 거듭제곱 (base^exp mod m) 
 */
function modPow(base, exp, m) {
  let res = 1;
  base %= m;
  while (exp > 0) {
    if (exp & 1) res = res * base % m;
    base = base * base % m;
    exp >>= 1;
  }
  return res;
}