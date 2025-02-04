import sys

k = int(sys.stdin.readline())
stacks = []

for _ in range(k):
    n = int(sys.stdin.readline())

    if n != 0:
        stacks.append(n)
    else:
        stacks.pop()

print(sum(stacks))
