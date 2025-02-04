import sys

def row(n, y):
    for i in range(9):
        if numArr[y][i] == n:
            return False
    return True

def column(n, x):
    for i in range(9):
        if numArr[i][x] == n:
            return False
    return True
def square(n, x, y):
    for i in range(3):
        for j in range(3):
            y1 = (y//3)*3+i
            x1 = (x//3)*3+j

            if numArr[y1][x1] == n:
                return False
    return True
def findNum(l):
    global numArr
    if l == len(empty):
        for arr in numArr:
            print(*arr)
        exit(0)


    for i in range(9):
        x = empty[l][1]
        y = empty[l][0]
        n = i+1

        if row(n, y) and column(n, x) and square(n, x, y):
            numArr[y][x] = n
            findNum(l+1)
            numArr[y][x] = 0

numArr = [ list(map(int, sys.stdin.readline().split())) for _ in range(9) ]
empty = []
for i in range(9):
    for j in range(9):
        if numArr[i][j] == 0:
            empty.append((i, j))



findNum(0)