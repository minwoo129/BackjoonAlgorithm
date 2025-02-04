import sys

n, b = map(int, sys.stdin.readline().split())
a = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]
c = 1000


def get_column(matrixA, matrixB, idxA, l, curArr):
    if l == n:
        return curArr
    num = 0
    for i in range(n):
        num += (matrixA[idxA][i] * matrixB[i][l]) % c
    num %= c
    curArr.append(num)
    return get_column(matrixA, matrixB, idxA, l+1, curArr)

def get_row(matrixA, matrixB, l, curArr):
    if l == n:
        return curArr

    column = get_column(matrixA, matrixB, l, 0, [])
    curArr.append(column)
    return get_row(matrixA, matrixB, l+1, curArr)

def multi_matrix(p):
    if p == 1:
        curArr = []
        for arr in a:
            newArr = [ num % c for num in arr ]
            curArr.append(newArr)

        return curArr

    tmp = multi_matrix(p//2)

    if p % 2 == 0:
        return get_row(tmp, tmp, 0, [])
    else:
        newMatrix = get_row(tmp, tmp, 0, [])
        return get_row(newMatrix, a, 0, [])

answer = multi_matrix(b)

for arr in answer:
    print(' '.join(map(str, arr)))