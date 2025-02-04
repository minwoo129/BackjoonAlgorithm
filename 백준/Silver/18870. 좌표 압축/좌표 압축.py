import sys

n = int(sys.stdin.readline())
coords = list(map(int, sys.stdin.readline().split()))
coordDics = {}
sortedCoords = coords[:]
answer = []
sortedCoords = list(set(sortedCoords))
sortedCoords.sort()

for i in range(len(sortedCoords)):
    num = sortedCoords[i]
    coordDics[num] = i

for coord in coords:
    answer.append(coordDics[coord])
print(' '.join(map(str, answer)))