function solution(food) {
    var answer = '';
    let foods = ['0'];
    let cnts = []
    
    for(let i = 1; i < food.length; i++) {
        const cnt = Math.floor(food[i]/2);
        cnts.push(cnt);
    }
    
    for(let i = cnts.length-1; i >= 0; i--) {
        const num = `${i+1}`;
        const arr = Array.from({length: cnts[i]}, () => num);
        foods.splice(0,0,...arr);
        foods = [ ...foods, ...arr ];
    }

    return foods.join('');
}