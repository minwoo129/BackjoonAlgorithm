def solution(order):
    answer = 0
    stack = []
    n = len(order)
    idx = 0
    
    for i in range(n):
        val = i+1
        stack.append(val)
        
        while len(stack) > 0 and stack[-1] == order[idx]:
            stack.pop()
            answer += 1
            idx += 1
    return answer