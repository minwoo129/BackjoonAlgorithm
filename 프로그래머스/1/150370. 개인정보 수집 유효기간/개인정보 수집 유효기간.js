function solution(today, terms, privacies) {
    var answer = [];
    // const date = new Date(today);
    // const date1 = new Date('2022.07.20');
    // console.log('date: ', date);
    // console.log('date1: ', date1);
    // let diff = date1.getTime() - date.getTime();
    // diff = diff/(1000*60*60*24)
    // console.log('diff: ', diff)
    let termData = {};
    for(let term of terms) {
        const [type, limit] = term.split(' ');
        termData[type] = parseInt(limit);
    }
    
    for(let i = 0; i < privacies.length; i++) {
        const privacy = privacies[i];
        answer = checkValid({privacy, idx: i+1, today, termData, answer})
    }
    
    return answer;
}

function checkValid({privacy, idx, today, termData, answer}) {
    const [date, type] = privacy.split(' ');
    const expireDate = new Date(date);
    expireDate.setMonth(expireDate.getMonth()+termData[type]);
    expireDate.setDate(expireDate.getDate()-1);
    const todayDate = new Date(today);
    
    if(expireDate.getTime() < todayDate.getTime()) answer.push(idx);
    
    return answer
    
    
}