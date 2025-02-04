def solution(cap, n, deliveries, pickups):
    answer = 0
    
    while len(deliveries) > 0 or len(pickups) > 0:
        w = cap
        dis1 = 0
        dis2 = 0
        
        for i in range(len(deliveries)-1, -1, -1):
            if deliveries[i] != 0:
                if w == cap:
                    dis1 = i+1
                if deliveries[i] <= w:
                    w -= deliveries[i]
                    deliveries.pop()
                else:
                    deliveries[i] -= w
                    break
            else:
                deliveries.pop()
                
        w = cap
        for i in range(len(pickups)-1, -1, -1):
            if pickups[i] != 0:
                if w == cap:
                    dis2 = i+1
                if pickups[i] <= w:
                    w -= pickups[i]
                    pickups.pop()
                else:
                    pickups[i] -= w
                    break
            else:
                pickups.pop()
        
        answer += (max(dis1, dis2)*2)
    return answer