// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let K = -1
	let dp = new Array(K+1).fill(0)
	for await (const line of rl) {
		K = line*1
		rl.close();
	}
	
	dp[1] = 0
	dp[2] = 1
	
	for(let i = 3; i <= K; i++) {
		dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
	}
	
	console.log(dp[K])
	
	process.exit();
})();
