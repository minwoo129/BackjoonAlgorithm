function solution(strlist) {
    var answer = [];
    return strlist.reduce((result, item) => {
        result = [ ...result, item.length ];
        return result;
    }, []);
}