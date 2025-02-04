import sys

n, m = map(int, sys.stdin.readline().split())
numArr = [ i+1 for i in range(n) ]
results = []

def findValues(a, l):

    if l == m:
        results.append(tuple(a))
        return

    for num in numArr:
        newArr = a[:]
        newArr.append(num)
        findValues(newArr, l+1)


findValues([], 0)
results = list(set(results))
results.sort()

for item in results:
    print(' '.join(map(str, list(item))))