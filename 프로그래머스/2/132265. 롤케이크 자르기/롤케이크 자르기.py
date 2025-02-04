from collections import Counter

def solution(topping):
    answer = 0
    a = Counter(topping)
    b = set([])
    
    for item in topping:
        a[item] -= 1
        b.add(item)
        
        if a[item] == 0:
            del a[item]
        
        if len(a) == len(b):
            answer += 1
    return answer