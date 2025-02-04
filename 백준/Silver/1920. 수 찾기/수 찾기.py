import sys

n = int(sys.stdin.readline())
numArr1 = list(map(int, sys.stdin.readline().split()))
cardMap = {}

for n in numArr1:
    if n not in cardMap:
        cardMap[n] = 1

m = int(sys.stdin.readline())
numArr2 = list(map(int, sys.stdin.readline().split()))

for n in numArr2:
    if n in cardMap:
        print(1)
    else:
        print(0)