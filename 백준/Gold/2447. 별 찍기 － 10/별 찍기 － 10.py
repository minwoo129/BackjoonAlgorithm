import sys
import math

def print_starmap(k):

    if k == 3:
        return [
            ['*', '*', '*'],
            ['*', ' ', '*'],
            ['*', '*', '*']
        ]

    itemStarMap = print_starmap(k // 3)
    newStarMap = []

    idxCnt = k // 3
    for i in range(k):
        idxArr = itemStarMap[i%idxCnt][:]
        if i // idxCnt != 1:
            inputArr = idxArr[:] * 3
            newStarMap.append(inputArr)
        else:
            inputArr = idxArr[:]
            inputArr += [' ']*idxCnt
            inputArr += idxArr[:]
            newStarMap.append(inputArr)

    return newStarMap


n = int(sys.stdin.readline())

starmap = print_starmap(n)

for arr in starmap:
    print(''.join(map(str, arr)))
