from heapq import heappush, heappop

def solution(n, k, enemy):
    answer = 0
    heap = []
    
    for e in enemy:
        n -= e
        if n >= 0:
            heappush(heap, -e)
        else:
            if k > 0:
                k -= 1
                heappush(heap, -e)
                n -= heappop(heap)
            else:
                break
        answer += 1
    return answer