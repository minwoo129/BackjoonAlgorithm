function solution(n, bans) {
    // 특정 길이의 모든 가능한 문자열 개수 계산
    function countPossibleStrings(length) {
        return BigInt(Math.pow(26, length));
    }

    // 특정 길이까지의 누적 문자열 개수 계산
    function getTotalCountUpToLength(length) {
        let total = 0n;
        for (let i = 1; i <= length; i++) {
            total += countPossibleStrings(i);
        }
        return total;
    }

    // 문자열이 n번째보다 앞에 있는지 확인
    function isBeforeN(str, n) {
        const strLength = str.length;
        let count = 0n;
        
        // str보다 짧은 길이의 모든 문자열 개수
        for (let i = 1; i < strLength; i++) {
            count += countPossibleStrings(i);
        }
        
        // str과 같은 길이의 사전순으로 이전 문자열 개수
        for (let i = 0; i < strLength; i++) {
            const currentChar = str.charCodeAt(i) - 97; // 'a'는 0
            count += BigInt(currentChar) * countPossibleStrings(strLength - i - 1);
        }
        
        return count < BigInt(n);
    }

    // 특정 위치의 문자열 생성
    function generateString(position, length) {
        let result = '';
        let remaining = position;
        
        for (let i = 0; i < length; i++) {
            const possibilities = Math.pow(26, length - i - 1);
            const charIndex = Math.floor(remaining / possibilities);
            result += String.fromCharCode(97 + charIndex);
            remaining %= possibilities;
        }
        
        return result;
    }

    // n을 BigInt로 변환
    n = BigInt(n);
    
    // banned된 문자열들을 정렬
    bans.sort((a, b) => a.length - b.length || a.localeCompare(b));
    
    // banned된 문자열들의 영향을 고려하여 실제 위치 계산
    let adjustedN = n;
    for (const ban of bans) {
        if (isBeforeN(ban, Number(adjustedN))) {
            adjustedN++;
        }
    }

    // 결과 문자열의 길이 찾기
    let resultLength = 1;
    let totalCount = 0n;
    while (totalCount < adjustedN) {
        totalCount += countPossibleStrings(resultLength);
        resultLength++;
    }
    resultLength--;

    // 해당 길이에서의 정확한 위치 계산
    let position = Number(adjustedN - (totalCount - countPossibleStrings(resultLength)));
    
    // 최종 문자열 생성
    return generateString(position - 1, resultLength);
}