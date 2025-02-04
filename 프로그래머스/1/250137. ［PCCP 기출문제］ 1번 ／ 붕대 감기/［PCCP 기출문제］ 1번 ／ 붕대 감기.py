def solution(bandage, health, attacks):
    answer = health
    
    t, x, y = bandage
    successCnt = 0
    attackIdx = 0
    
    maxTime = attacks[-1][0]+1
    
    for i in range(maxTime):
        time, attack = attacks[attackIdx]

        if i == time:
            successCnt = 0
            answer -= attack
            attackIdx += 1
            if answer <= 0:
                return -1
            continue
        
        successCnt += 1
        if answer + x <= health:
            answer += x
        else:
            answer = health
        
        if successCnt == t:
            successCnt = 0
            
            if answer + y <= health:
                answer += y
            else:
                answer = health

    return answer