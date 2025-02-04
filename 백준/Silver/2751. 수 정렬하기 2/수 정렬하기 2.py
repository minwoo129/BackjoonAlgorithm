import sys

n = int(sys.stdin.readline())
numArr = []

for _ in range(n):
    numArr.append(int(sys.stdin.readline()))
    
numArr.sort()

for num in numArr:
    print(num)