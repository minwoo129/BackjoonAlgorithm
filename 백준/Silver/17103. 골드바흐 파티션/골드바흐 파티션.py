import sys, math

def get_primes():
    maxVal = 1000001
    primes = [ True for _ in range(maxVal) ]

    primes[0] = primes[1] = False

    end = int(math.sqrt(maxVal))
    for i in range(2, end+1):
        if primes[i]:
            for j in range(i*i, maxVal, i):
                primes[j] = False
    return primes

primes = get_primes()

t = int(sys.stdin.readline())
counts = []
for _ in range(t):
    n = int(sys.stdin.readline())
    count = 0
    for i in range(2, n//2+1):
        if primes[i] and primes[n-i]:
            count += 1
    counts.append(count)

print('\n'.join(map(str, counts)))
