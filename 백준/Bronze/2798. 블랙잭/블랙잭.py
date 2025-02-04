n, m = map(int, input().split())
numArr = list(map(int, input().split()))
answer = 0

for i in range(0, n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sumValue = numArr[i] + numArr[j] + numArr[k]
            if sumValue > m:
                continue
            answer = max(answer, sumValue)
     
print(answer)
