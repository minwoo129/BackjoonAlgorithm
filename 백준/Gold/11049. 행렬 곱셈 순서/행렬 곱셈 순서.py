import sys
import heapq

n = int(sys.stdin.readline())
arr = []
board = [[0] * n for _ in range(n)]

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    arr.append((a, b))
for i in range(1, n):
    board[i-1][i] = arr[i-1][0] * arr[i-1][1] * arr[i][1]

for term in range(2, n):
    for start in range(n):
        if start + term == n:
            break
        i = start
        j = start+term
        board[i][j] = 1e9
        for k in range(i, j):
            board[i][j] = min(board[i][j], board[i][k] + board[k+1][j] + (arr[i][0] * arr[k+1][0] * arr[j][1]))
print(board[0][n-1])