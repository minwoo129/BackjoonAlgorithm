// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let cntG = 0, cntB = 0
	for await (const line of rl) {
		const [G, B] = line.split(' ').map(item => item*1)
		cntG = G
		cntB = B
		rl.close();
	}
	
	if(cntG > cntB) {
		console.log('Goorm')
	}
	else if(cntG < cntB) {
		console.log('Baram')
	}
	else {
		console.log('Tie')
	}
	process.exit();
})();
