import sys

a = int(sys.stdin.readline())
numArr = list(map(int, sys.stdin.readline().split()))

numArr.sort()

answer = numArr[0] * numArr[-1]

print(answer)