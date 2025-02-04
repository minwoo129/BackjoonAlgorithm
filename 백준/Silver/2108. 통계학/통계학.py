import sys

n = int(sys.stdin.readline())
medianMap = {}
numArr = []

# 평균
avr = 0
# 중앙값
mid = 0
# 최빈값
medianVal = 0
# 범위
rangeVal = 0

for _ in range(n):
    num = int(sys.stdin.readline())
    numArr.append(num)
    avr += num
    if num in medianMap:
        medianMap[num] += 1
    else:
        medianMap[num] = 1

numArr.sort()
avr = round(avr / n)
medians = [ (key, value) for key, value in medianMap.items() ]
maxMedian = max(list(medianMap.values()))

medians = sorted(medians, key = lambda item: item[0])

mid = numArr[n // 2]

rangeVal = medians[-1][0] - medians[0][0]

medians = [ item for item in medians if item[1] == maxMedian ]

if len(medians) > 1:
    medianVal = medians[1][0]
else:
    medianVal = medians[0][0]

print(avr)
print(mid)
print(medianVal)
print(rangeVal)
