// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let inputs = []
	for await (const line of rl) {
		inputs.push(line)
		rl.close();
	}
	
	const [N, S] = inputs
	const n = parseInt(N);
	let answer = ''
	
	let sArr = S.split('')
	while(sArr.length > 1) {
		const ch1 = sArr.shift()
		const ch2 = sArr[0]
		
		if(ch1 === ch2) {
			answer += ch1.toUpperCase()
			answer += ch2.toUpperCase()
			sArr.shift()
		}
		else {
			answer += ch1
		}
	}
	
	if(sArr.length > 0) {
		answer += sArr.shift()
	}
	
	console.log(answer)

	
	process.exit();
})();
