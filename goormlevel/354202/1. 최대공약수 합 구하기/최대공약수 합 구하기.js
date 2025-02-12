// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let inputs = []
	for await (const line of rl) {
		inputs.push(line)
		rl.close();
	}
	const N = inputs[0] * 1
	const values = inputs[1].split(' ').map(item => item*1)
	
	function getGCD(a,b) {
		return b === 0 ? a : getGCD(b, a % b)
	}
	
	let answer = 0
	for(let i = 0; i < values.length; i++) {
		for(let j = i+1; j < values.length; j++) {
			answer += getGCD(values[i], values[j])
		}
	}
	
	console.log(answer)
	
	process.exit();
})();
