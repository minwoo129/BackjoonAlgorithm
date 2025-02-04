import sys

n, m = map(int, sys.stdin.readline().split())
a = set(list(map(int, sys.stdin.readline().split())))
b = set(list(map(int, sys.stdin.readline().split())))

answer = 0
answer += len(a-b)
answer += len(b-a)

print(answer)