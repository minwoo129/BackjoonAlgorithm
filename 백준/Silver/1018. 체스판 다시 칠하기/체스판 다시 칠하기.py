import sys

n, m = map(int, sys.stdin.readline().split())
inputMap = []
answer = 64
mapA = []
mapB = []

for i in range(n):
    inputMap.append(list(sys.stdin.readline()))

for i in range(8):
    if i % 2 == 0:
        mapA.append(['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'])
        mapB.append(['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'])
    else:
        mapA.append(['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'])
        mapB.append(['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'])

for i in range(n-7):
    for j in range(m-7):
        cntA = 0
        cntB = 0
        for x in range(8):
            for y in range(8):
                if inputMap[i+x][j+y] != mapA[x][y]:
                    cntA += 1
                else:
                    cntB += 1
        answer = min(answer, cntA, cntB)
print(answer)