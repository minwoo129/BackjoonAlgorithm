n = int(input())
answer = n

def convertNum(num):
    nums = list(map(int, str(num)))
    sums = num
    sums += sum(nums)
    
    return sums

for num in range(n, 0, -1):
    m = convertNum(num)
    if m == n:
        answer = min(answer, num)

if answer == n:
    answer = 0
print(answer)
        
    