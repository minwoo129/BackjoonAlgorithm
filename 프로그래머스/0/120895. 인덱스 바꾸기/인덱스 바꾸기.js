function solution(my_string, num1, num2) {
    let answer = '';
    let myStrArr = my_string.split('');
    const shiftChar = myStrArr[num2];
    myStrArr[num2] = myStrArr[num1];
    myStrArr[num1] = shiftChar;
    return myStrArr.join('');
}