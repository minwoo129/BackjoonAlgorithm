// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let n = -1
	let sum = 0
	for await (const line of rl) {
		if(n === -1) {
			n = line * 1
		}
		else {
			sum = [...line.split(' ').map(item => item * 1)].reduce((a,b) => a+b)
		}
		rl.close();
	}
	
	console.log(sum.toString(8))
	
	process.exit();
})();
