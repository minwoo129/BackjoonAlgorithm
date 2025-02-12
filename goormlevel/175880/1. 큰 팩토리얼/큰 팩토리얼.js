// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let N = -1;
	for await (const line of rl) {
		N = line*1;
		rl.close();
	}
	
	const C = 1000000007
	
	let answer = 1
	
	for(let i = 1; i <= N; i++) {
		answer = ((answer * i) % C)
	}
	console.log(answer)
	
	process.exit();
})();
