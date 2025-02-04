import sys

n, c = map(int, sys.stdin.readline().split())
points = [ int(sys.stdin.readline()) for _ in range(n) ]

points.sort()

start = 1
end = points[-1] - points[0]

while start <= end:
    mid = (start + end) // 2
    count = 1
    currentPoint = points[0]

    for i in range(1, len(points)):
        if points[i] >= currentPoint + mid:
            count += 1
            currentPoint = points[i]

    if count >= c:
        start = mid+1

    else:
        end = mid-1

print(end)

