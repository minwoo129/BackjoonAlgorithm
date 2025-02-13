// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let A = -1, B = -1;
	for await (const line of rl) {
		const [a, b] = line.split(' ').map(item => item * 1)
		A = a
		B = b;
		rl.close();
	}
	
	console.log((A+B).toFixed(6))
	
	process.exit();
})();
