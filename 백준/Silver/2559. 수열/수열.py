import sys

n, k = map(int, sys.stdin.readline().split())
tempArr = list(map(int, sys.stdin.readline().split()))
sumArr = []

sumArr.append(sum(tempArr[:k]))

for i in range(n-k):
    sumArr.append(sumArr[i] - tempArr[i] + tempArr[i+k])

print(max(sumArr))
