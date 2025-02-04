import sys

n, m = map(int, sys.stdin.readline().split())
numArr = [ i+1 for i in range(n) ]
results = []

def findValues(a, idx, l):

    if l == m:
        print(' '.join(map(str, a)))
        return

    for i in range(len(numArr)):
        newArr = a[:]
        if i < idx:
            continue
        newArr.append(numArr[i])
        findValues(newArr, i, l+1)


findValues([], 0, 0)