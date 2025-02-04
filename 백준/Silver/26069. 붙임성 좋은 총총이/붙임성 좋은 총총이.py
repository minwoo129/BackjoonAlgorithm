import sys

n = int(sys.stdin.readline())
dance = {"ChongChong"}

for _ in range(n):
    a, b = sys.stdin.readline().rstrip().split()

    if a in dance:
        dance.add(b)
    if b in dance:
        dance.add(a)

print(len(dance))