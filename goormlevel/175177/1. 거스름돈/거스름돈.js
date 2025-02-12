// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let input = 0
	for await (const line of rl) {
		input = line * 1;
		rl.close();
	}
	
	const coins = [40, 20, 10, 5, 1]
	
	let answer = 0
	for(let coin of coins) {
		if(input === 0) {
			break;
		}
		answer += Math.floor(input / coin)
		input = input % coin;
	}
	
	console.log(answer)
	
	process.exit();
})();
