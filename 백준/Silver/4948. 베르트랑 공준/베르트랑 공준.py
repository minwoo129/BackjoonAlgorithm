import sys, math

def get_primes():
    maxVal = 123456 * 2
    primes = [ True for _ in range(maxVal+1) ]
    primes[0] = primes[1] = False

    end = int(math.sqrt(maxVal))
    for i in range(2, end+1):
        if primes[i]:
            for j in range(i*i, maxVal+1, i):
                primes[j] = False

    return primes

primes = get_primes()

def get_prime_counts(n):
    count = 0

    for i in range(n+1, n*2+1):
        count += 1 if primes[i] else 0

    return count

answers = []

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    answers.append(get_prime_counts(n))

for cnt in answers:
    print(cnt)

