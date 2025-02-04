import sys
input = sys.stdin.readline
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
sumArr = [ 0 ]
sum = 0

for i in numbers:
    sum += i
    sumArr.append(sum)

for _ in range(m):
    s, e = map(int, input().split())
    print(sumArr[e] - sumArr[s-1])