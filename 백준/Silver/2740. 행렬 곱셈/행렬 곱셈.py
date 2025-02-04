import sys

n, m = map(int, sys.stdin.readline().split())
A = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]
m, k = map(int, sys.stdin.readline().split())
B = [ list(map(int, sys.stdin.readline().split())) for _ in range(m) ]

answer = []

def get_column(idxA, l, curArr):
    if l == k:
        return curArr

    num = 0
    for i in range(m):
        num += (A[idxA][i] * B[i][l])
    curArr.append(num)
    return get_column(idxA, l+1, curArr)

def get_row(l):
    if l == n:
        for arr in answer:
            print(' '.join(map(str, arr)))
        return
    column = get_column(l, 0, [])
    answer.append(column)
    get_row(l+1)

get_row(0)




