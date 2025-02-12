// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let N = -1, M = -1;
	let dozens = []
	let onePieces = []
	for await (const line of rl) {
		const [A, B] = line.split(' ').map(item => item*1)
		if(N === -1) {
			N = A;
			M = B;
		}
		else {
			dozens.push(A)
			onePieces.push(B)
		}
		rl.close();
	}
	
	const minDozenPrice = Math.min(...dozens)
	const minPiecePrice = Math.min(...onePieces)
	
	let answer = 0
	
	const dozenCnt = Math.floor(N / 12)
	const priceCases = [
		(dozenCnt+1) * minDozenPrice, // N보다 많이 구매하는 경우 => 한다스당 최소금액으로
		dozenCnt * minDozenPrice + (N % 12) * minPiecePrice, // 개수를 맞춰서 구매하는 경우 ==> 한 다스: 다스당 최소금액, 남은 것들: 한 자루당 최소금액 
		N * minPiecePrice, // 개수를 맞춰서 구매하는 경우 => 모든 볼펜을 한 자루당 최소금액으로 구매
	]
	
	answer = Math.min(...priceCases)

	console.log(answer)
	process.exit();
})();
