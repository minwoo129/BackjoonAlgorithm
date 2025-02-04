import sys, math

n = int(sys.stdin.readline())
nums = [ int(sys.stdin.readline()) for _ in range(n) ]

def check_is_prime_num(n):
    if n < 2:
        return False
    
    end = int(math.sqrt(n))

    for i in range(2, end+1):
        if n % i == 0:
            return False
    return True

idx = nums[0]
count = 0
while True:
    if check_is_prime_num(idx):
        print(idx)
        count += 1

        if count == n:
            break
        else:
            idx = nums[count]
    else:
        idx += 1


