import sys

n = int(sys.stdin.readline())
inputArr = []

for _ in range(n):
    inputArr.append(list(map(int, sys.stdin.readline().split())))

inputArr = sorted(inputArr, key = lambda x : (x[1], x[0]))

for numArr in inputArr:
    print(' '.join(map(str, numArr)))