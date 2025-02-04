import sys
import heapq

c = int(sys.stdin.readline())

def calculateAnswer(n:int, files: list[int]):
    board = [ [0]*(n+1) for _ in range(n+1) ]
    s_list = [ 0 for _ in range(n+1) ]
    for i in range(1, n+1):
        s_list[i] = s_list[i-1] + files[i-1]

    for i in range(1, n):
        board[i][i+1] = files[i-1] + files[i]

    for term in range(2, n):
        for start in range(1, n):
            if start + term > n:
                break
            i = start
            j = start + term

            board[i][j] = min([ board[i][k] + board[k+1][j] for k in range(i, j) ]) + (s_list[j] - s_list[i-1])
    print(board[1][-1])

for _ in range(c):
    n = int(sys.stdin.readline())
    files = list(map(int, sys.stdin.readline().split()))
    calculateAnswer(n, files)