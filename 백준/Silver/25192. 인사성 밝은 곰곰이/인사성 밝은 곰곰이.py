import sys

n = int(sys.stdin.readline())
memberMap = {}
answer = 0

for _ in range(n):
    inputVal = sys.stdin.readline().rstrip()

    if inputVal == 'ENTER':
        memberMap = {}
        continue

    if inputVal not in memberMap:
        memberMap[inputVal] = 1
        answer += 1
        continue

print(answer)