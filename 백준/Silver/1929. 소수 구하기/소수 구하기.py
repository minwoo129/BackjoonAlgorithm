import sys, math

m, n = map(int, sys.stdin.readline().split())

def find_primes(maxVal):
    primes = [ True for _ in range(maxVal+1) ]
    primes[0] = primes[1] = False

    end = int(math.sqrt(maxVal))

    for i in range(2, end+1):
        if primes[i]:
            for j in range(i*i, maxVal+1, i):
                primes[j] = False

    return primes

primes = find_primes(n)

for i in range(m, n+1):
    if primes[i]:
        print(i)


