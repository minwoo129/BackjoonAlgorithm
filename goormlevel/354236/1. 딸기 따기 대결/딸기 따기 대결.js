// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let cntG = 0, cntB = 0
	
	for await (const line of rl) {
		const [A, B, C, D] = line.split(' ').map(item => item*1)
		cntG = A*B
		cntB = C*D
		rl.close();
	}
	
	if(cntG > cntB) {
		console.log('G')
	}
	else if(cntG < cntB) {
		console.log('B')
	}
	else {
		console.log('D')
	}
	
	
	process.exit();
})();
