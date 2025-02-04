import sys

n = int(sys.stdin.readline())
c = 1000000007

def get_column(matrixA, matrixB, idxA, l, curArr):
    if l == 2:
        return curArr
    num = 0
    for i in range(2):
        num += (matrixA[idxA][i] * matrixB[i][l]) % c
    num %= c
    curArr.append(num)
    return get_column(matrixA, matrixB, idxA, l+1, curArr)

def get_row(matrixA, matrixB, l, curArr):
    if l == 2:
        return curArr

    column = get_column(matrixA, matrixB, l, 0, [])
    curArr.append(column)
    return get_row(matrixA, matrixB, l+1, curArr)

def get_fibonacci(n):
    if n == 1:
        return [[1, 1], [1, 0]]

    tmp = get_fibonacci(n//2)

    if n % 2 == 0:
        return get_row(tmp, tmp, 0, [])
    else:
        tmp1 = get_row(tmp, tmp, 0, [])
        tmp2 = get_fibonacci(1)

        return get_row(tmp1, tmp2, 0, [])

fibonacci_arr = get_fibonacci(n)
print(fibonacci_arr[0][1])
