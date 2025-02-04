function solution(t, p) {
    var answer = 0;
    let slices = [];
    for(let i = 0; i <= t.length-p.length; i++) {
        slices.push(parseInt(t.slice(i, i+p.length)))
    }
    slices = slices.filter(item => item <= parseInt(p))
    return slices.length;
}