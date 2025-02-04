import sys

n = int(sys.stdin.readline())
i = 0
curNum = 666
answer = 0

while i < n:
    curNums = str(curNum)

    if '666' in curNums:
        answer = curNums
        i += 1
    curNum += 1
print(answer)