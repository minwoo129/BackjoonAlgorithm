import sys, math

k, n = map(int, sys.stdin.readline().split())
numArr = [int(sys.stdin.readline()) for _ in range(k)]

start = 1
end = max(numArr)


while start <= end:
    mid = (start + end) // 2
    sumVal = 0

    for num in numArr:
        sumVal += (num // mid)

    if sumVal >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)