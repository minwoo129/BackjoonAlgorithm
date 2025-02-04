import sys

inputVal = int(sys.stdin.readline())
nStrArr = list(str(inputVal))
nArr = list(map(int, nStrArr))

nArr.sort(reverse=True)

print(''.join(map(str, nArr)))

