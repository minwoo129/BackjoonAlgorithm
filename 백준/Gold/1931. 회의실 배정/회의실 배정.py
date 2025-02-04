import sys
from collections import deque

n = int(sys.stdin.readline())
inputDatas = []

for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    inputDatas.append((start, end))

inputDatas = sorted(inputDatas, key= lambda x: (x[1], x[0]))
results = []

results.append(inputDatas[0])

for i in range(1, len(inputDatas)):
    start1, end1 = results[-1]
    start2, end2 = inputDatas[i]

    if end1 <= start2:
        results.append((start2, end2))

print(len(results))
