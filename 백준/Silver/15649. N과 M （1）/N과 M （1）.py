import sys

n, m = map(int, sys.stdin.readline().split())
numArr = [ i+1 for i in range(n) ]
results = []

def findValues(a, l):

    if l == m:
        print(' '.join(map(str, a)))
        return

    for num in numArr:
        newArr = a[:]
        if num in newArr:
            continue
        newArr.append(num)
        findValues(newArr, l+1)


findValues([], 0)
