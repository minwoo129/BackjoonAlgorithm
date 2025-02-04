import sys

n, m = map(int, sys.stdin.readline().split())
nameMap1 = {}
names = []

for i in range(n):
    nameMap1[sys.stdin.readline().rstrip()] = 1
for i in range(m):
    name = sys.stdin.readline().rstrip()

    if name in nameMap1:
        names.append(name)
names.sort()
print(len(names))
for name in names:
    print(name)