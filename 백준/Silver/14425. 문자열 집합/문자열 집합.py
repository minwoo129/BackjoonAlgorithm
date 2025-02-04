import sys

n, m = map(int, sys.stdin.readline().split())
dictS = {}

answer = 0

for _ in range(n):
    inputVal = sys.stdin.readline().rstrip()
    dictS[inputVal] = 1

for _ in range(m):
    inputVal1 = sys.stdin.readline().rstrip()
    answer += 1 if inputVal1 in dictS else 0
print(answer)