import sys

numArr = []
max_idx = 5

for i in range(max_idx):
    numArr.append(int(sys.stdin.readline()))

numArr.sort()
avr = sum(numArr) // 5
mid = numArr[2]

print(avr)
print(mid)