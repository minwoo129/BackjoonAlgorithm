import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
start = 1
end = max(trees)
cases = []


while start <= end:
    mid = (start + end) // 2
    sumVal = 0

    for tree in trees:
        v = tree - mid
        if v >= 0:
            sumVal += v
        if sumVal > m:
            break

    if sumVal >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)