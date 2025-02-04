import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
d = ['d', 'l', 'r', 'u']
answer = 'z'

def isValid(n, m, x, y):
    return x >= 1 and x <= n and y >= 1 and y <= m

def DFS(n, m, x, y, r, c, k, L, dirs):
    global answer
    
    if k < L+abs(x-r)+abs(y-c):
        return
    if x == r and y == c and L == k:
        answer = dirs
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if isValid(n, m, nx, ny) and dirs < answer:
            DFS(n, m, nx, ny, r, c, k, L+1, dirs + d[i])
        
    
def solution(n, m, x, y, r, c, k):
    dist = abs(x-r) + abs(y-c)
    
    if dist > k or (k - dist)%2 == 1:
        return 'impossible'
    DFS(n, m, x, y, r, c, k, 0, '')
    
    return answer