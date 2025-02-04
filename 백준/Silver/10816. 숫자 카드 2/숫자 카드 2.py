import sys

n = int(sys.stdin.readline())
cards1 = list(map(int, sys.stdin.readline().split()))
cards1Map = {}

for num in cards1:
    if num in cards1Map:
        cards1Map[num] += 1
    else:
        cards1Map[num] = 1

m = int(sys.stdin.readline())
cards2 = list(map(int, sys.stdin.readline().split()))
answer = []

for num in cards2:
    if num in cards1Map:
        answer.append(cards1Map[num])
    else:
        answer.append(0)

print(' '.join(map(str, answer)))