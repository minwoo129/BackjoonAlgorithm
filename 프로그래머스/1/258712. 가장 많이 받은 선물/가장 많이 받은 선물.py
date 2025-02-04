def solution(friends, gifts):
    answer = 0
    idxMap = {}
    friendCnt = len(friends)
    presentCnt = [ [ 0 for _ in range(friendCnt) ] for _ in range(friendCnt) ]
    rank = [ 0 for _ in range(friendCnt) ]
    getCnt = [ 0 for _ in range(friendCnt) ]
    
    for i in range(friendCnt):
        idxMap[friends[i]] = i
        presentCnt[i][i] = -1
    
    for giftValue in gifts:
        fromGift, toGift = giftValue.split()

        presentCnt[idxMap[fromGift]][idxMap[toGift]] += 1
        rank[idxMap[fromGift]] += 1
        rank[idxMap[toGift]] -= 1
    
    
    for i in range(friendCnt):
        dataArr = presentCnt[i]
        dataSetArr = list(set(dataArr[:]))
        
        if len(dataSetArr) == 1 and dataSetArr[0] == -1:
            continue
        
        for j in range(friendCnt):
            if dataArr[j] == -1:
                continue
            
            a = presentCnt[i][j]
            b = presentCnt[j][i]
            
            if a > b:
                getCnt[i] += 1
            elif a < b:
                getCnt[j] += 1
            elif a == b:
                rankA = rank[i]
                rankB = rank[j]
                
                if rankA > rankB:
                    getCnt[i] += 1
                elif rankA < rankB:
                    getCnt[j] += 1
            presentCnt[i][j] = -1
            presentCnt[j][i] = -1
    
    return max(getCnt)