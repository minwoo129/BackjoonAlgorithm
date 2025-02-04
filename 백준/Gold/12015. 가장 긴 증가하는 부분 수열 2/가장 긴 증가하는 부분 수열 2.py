import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

results = [0]

for case in A:
    if results[-1] < case:
        results.append(case)
    else:
        start = 0
        end = len(results)

        while start < end:
            mid = (start+end)//2

            if results[mid] < case:
                start = mid+1
            else:
                end = mid
        results[end] = case

print(len(results)-1)