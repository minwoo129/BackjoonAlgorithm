import sys

n, m = map(int, sys.stdin.readline().split())
vocaMap = {}

for _ in range(n):
    voca = sys.stdin.readline().rstrip()

    if len(voca) < m:
        continue

    if voca in vocaMap:
        vocaMap[voca] += 1
    else:
        vocaMap[voca] = 1

vocas = [ (key, value) for key, value in vocaMap.items() ]

vocas = sorted(vocas, key = lambda item: (-item[1], -len(item[0]), item[0]))
vocaValues = [ voca[0] for voca in vocas ]

print('\n'.join(map(str, vocaValues)))
