// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let input = []
	for await (const line of rl) {
		const inputArr = line.split(' ').map(item => item * 1)
		input = [...inputArr];
		rl.close();
	}
	
	const [A, B] = input;
	let answer = 0
	answer += A*2
	
	answer += Math.PI * B
	console.log(Math.trunc(answer))
	
	process.exit();
})();
