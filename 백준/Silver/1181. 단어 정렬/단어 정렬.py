import sys

n = int(sys.stdin.readline())
vocaArr = []

for _ in range(n):
    vocaArr.append(sys.stdin.readline().rstrip())
vocaArr = list(set(vocaArr))

vocaArr.sort()
vocaArr.sort(key=len)

for voca in vocaArr:
    print(voca)