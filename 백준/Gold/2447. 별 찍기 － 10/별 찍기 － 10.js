const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim()

function printStarmap(k) {
    if(k === 3) {
        return [
            ['*', '*', '*'],
            ['*', ' ', '*'],
            ['*', '*', '*']
        ]
    }
    
    const itemStarMap = printStarmap(Math.floor(k / 3))
    let newStarMap = []
    
    const idxCnt = Math.floor(k / 3)
    for(let i = 0; i < k; i++) {
        let idxArr = itemStarMap[i % idxCnt]
        
        if(Math.floor(i / idxCnt) !== 1) {
            newStarMap.push([...idxArr, ...idxArr, ...idxArr])
        }
        else {
            let inputArr = [
                ...idxArr,
                ...Array.from({length: idxCnt}, () => ' '),
                ...idxArr
            ]
            newStarMap.push(inputArr)
        }
    }
    
    return newStarMap
}

const n = parseInt(inputs)

const starMap = printStarmap(n)

for(const arr of starMap) {
    console.log(arr.join(''))
}
