// Run by Node.js
const readline = require('readline');

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

let n = -1
let arr = []

rl.on('line', (line) => {
	if(n === -1) {
		n = line * 1;
	}
	else {
		arr.push([...line.split(' ').map(item => item * 1)])
	}
})

rl.on('close', () => {
	let result = 0
	let currentTime = -1
	
	arr.sort((a, b) => {
		if(a[1] === b[1]) return a[0] - b[0]
		else return a[1] - b[1]
	})
	
	for(const [start, end] of arr) {
		if(start > currentTime) {
			result++
			currentTime = end
		}
	}
	
	console.log(result)
})

