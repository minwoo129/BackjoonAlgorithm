import sys

n, k = map(int, sys.stdin.readline().split())
coins = [ int(sys.stdin.readline()) for _ in range(n) ]
coins.sort(reverse=True)
count = 0

for coin in coins:
    if coin <= k:
        count += k//coin
        k %= coin

        if k <= 0:
            break
print(count)
