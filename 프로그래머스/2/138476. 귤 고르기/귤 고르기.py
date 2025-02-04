def solution(k, tangerine):
    answer = 0
    cntData = {}
    
    for i in tangerine:
        if i in cntData:
            cntData[i] += 1
        else:
            cntData[i] = 1
    cntData = dict(sorted(cntData.items(), key = lambda item: item[1], reverse = True))
    
    for i in cntData:
        if k <= 0:
            return answer
        k -= cntData[i]
        answer += 1
    return answer