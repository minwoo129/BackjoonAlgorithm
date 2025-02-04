import sys

n = int(sys.stdin.readline())
card1 = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
card2 = list(map(int, sys.stdin.readline().split()))

card1Map = { num: 1 for num in card1 }
answer = []
for num in card2:
    if num in card1Map:
        answer.append(1)
    else:
        answer.append(0)
print(' '.join(map(str, answer)))