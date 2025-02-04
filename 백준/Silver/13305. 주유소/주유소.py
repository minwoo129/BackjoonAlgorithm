import sys

n = int(sys.stdin.readline())
routeLens = list(map(int, sys.stdin.readline().split()))
gas = list(map(int, sys.stdin.readline().split()))

minGasPrice = gas[0]
result = minGasPrice * routeLens[0]

for i in range(1, n-1):
    minGasPrice = gas[i] if minGasPrice > gas[i] else minGasPrice
    result += minGasPrice * routeLens[i]

print(result)
