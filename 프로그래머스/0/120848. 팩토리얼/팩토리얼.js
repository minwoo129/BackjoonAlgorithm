function solution(n) {
    var answer = 0;
    let num = 1, factorial = 1;
    while(n >= factorial) {
        factorial *= num;
        if(n >= factorial) num++
    }
    return num-1;
}