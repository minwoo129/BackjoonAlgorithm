import sys

n = int(sys.stdin.readline())
numArr = list(map(int, sys.stdin.readline().split()))
stacks = []
target = 1

for num in numArr:
    stacks.append(num)

    while stacks and stacks[-1] == target:
        stacks.pop()
        target += 1

if stacks:
    print("Sad")
else:
    print("Nice")