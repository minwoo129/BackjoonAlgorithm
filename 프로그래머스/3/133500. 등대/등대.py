from collections import defaultdict,deque

def solution(n, lighthouse):
    answer = 0
    graph = defaultdict(list)
    lights = [ 0 ] * (n+1)
    
    for [a,b] in lighthouse:
        graph[a].append(b)
        graph[b].append(a)
    
    q = deque()
    
    for i in range(1, n+1):
        if len(graph[i]) == 1:
            q.append(i)
    
    while q:
        now_leaf = q.popleft()
        
        if len(graph[now_leaf]) == 0:
            break
        parent = graph[now_leaf][0]
        del graph[now_leaf]
        graph[parent].remove(now_leaf)
        
        if len(graph[parent]) == 1:
            q.append(parent)
        
        if lights[now_leaf] == 1:
            continue
        lights[parent] = 1
    
    return sum(lights)