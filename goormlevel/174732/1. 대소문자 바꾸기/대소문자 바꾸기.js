// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let input = ''
	for await (const line of rl) {
		input = line;
		rl.close();
	}
	
	let answer = ''
	
	for(let ch of input) {
		if(ch === ch.toUpperCase()) {
			answer += ch.toLowerCase();
		}
		else {
			answer += ch.toUpperCase()
		}
	}
	
	console.log(answer)
	process.exit();
})();
