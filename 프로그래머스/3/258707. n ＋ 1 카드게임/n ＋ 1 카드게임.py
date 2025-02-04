from collections import deque

def solution(coin, cards):
    answer = 1
    n = len(cards)
    currentCards = set(cards[:n//3])
    notYets = deque(cards[n//3:])
    posibilities = set()
    
    def remove_check(currentCards, posibilities):
        for num in currentCards:
            if n+1-num in posibilities:
                currentCards.remove(num)
                posibilities.remove(n+1-num)
                return True
        return False
    
    while notYets:
        posibilities.add(notYets.popleft())
        posibilities.add(notYets.popleft())
        
        if remove_check(currentCards, currentCards):
            answer += 1
        elif coin >= 1 and remove_check(currentCards, posibilities):
            coin -= 1
            answer += 1
        elif coin >= 2 and remove_check(posibilities, posibilities):
            coin -= 2
            answer += 1
        else:
            break
        
        
    return answer