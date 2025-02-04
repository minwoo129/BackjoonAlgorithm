import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

start = 1
end = k
answer = 0

while start <= end:
    mid = (start+end) // 2
    cnt = 0

    for i in range(n):
        cnt += min(mid // (i+1), n)

    if cnt >= k:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)