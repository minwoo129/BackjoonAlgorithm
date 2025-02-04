import sys

n = int(sys.stdin.readline())
times = list(map(int, sys.stdin.readline().split()))

times.sort()

sumTimes = []
currentSum = 0
for time in times:
    sumTimes.append(currentSum+time)
    currentSum += time

print(sum(sumTimes))
