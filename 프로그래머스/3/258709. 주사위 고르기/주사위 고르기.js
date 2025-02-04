function allocateDices(n) {
    let results = []
    function allocate(l, arr, last) {
        if(l == Math.floor(n/2)) {
            results.push(arr)
            return
        }
        
        for(let i = 1; i <= n; i++) {
            if(i <= last) {
                continue
            }
            newArr = [...arr]
            newArr.push(i)
            allocate(l+1, newArr, i)
        }
    }
    allocate(0, [], 0)

    return results
}

function selectDice(dice, selectedDices) {
    let result = []
    
    for(let idx of selectedDices) {
        result.push([...dice[idx-1]])
    }
    
    return result
}

function calculateRollResult(dices) {
    let results = []
    
    function roll(l, sumVal) {
        if(l == dices.length) {
            results.push(sumVal)
            return
        }
        
        for(let num of dices[l]) {
            roll(l+1, sumVal+num)
        }
    }
    
    roll(0, 0)
    results.sort((a, b) => a-b)
    return results
}

function calculateResult(roll1, roll2) {
    let result = 0
    const map1 = convertRollToObject(roll1)
    const map2 = convertRollToObject(roll2)
    const mapArr1 = Object.entries(map1)
    const mapArr2 = Object.entries(map2)
    
    for(let [key1, cnt1] of mapArr1) {
        for(let [key2, cnt2] of mapArr2) {
            if(parseInt(key1) <= parseInt(key2)) {
                break
            }
            
            result += (cnt1*cnt2)
        }
    }
    
    return result
}

function convertRollToObject(roll) {
    let map = {}
    for(let val of roll) {
        const key = `${val}`
        
        if(!(key in map)) {
            map[key] = 0
        }
        
        map[key] += 1
    }
    
    return map
}

function solution(dice) {
    var answer = [];
    let n = dice.length
    let selectedDices = allocateDices(n)
    
    let len1 = selectedDices.length
    let maxVal = 0
    
    for(let i = 0; i < len1; i++) {
        let dice1 = selectDice(dice, selectedDices[i])
        let dice2 = selectDice(dice, selectedDices[len1-1-i])
        let roll1 = calculateRollResult(dice1)
        let roll2 = calculateRollResult(dice2)
        const result1 = calculateResult(roll1, roll2)
        
        if(result1 > maxVal) {
            maxVal = result1
            answer = selectedDices[i]
        }
    }
    return answer;
}