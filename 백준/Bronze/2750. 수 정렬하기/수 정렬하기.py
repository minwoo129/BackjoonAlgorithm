import sys

n = int(sys.stdin.readline())
numArr = []

for i in range(n):
    numArr.append(int(sys.stdin.readline()))
    
numArr.sort()
for num in numArr:
    print(num)