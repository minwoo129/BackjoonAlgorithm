import sys

n, k = map(int, sys.stdin.readline().split())
p = 1000000007

def factorial_with_rest(n):
    result = 1

    for i in range(1, n+1):
        result = ( (result * i) % p)
    return result

def reduce(n, c):
    if c == 1:
        return n % p

    tmp = reduce(n, c//2)

    if c % 2 == 0:
        return (tmp * tmp) % p
    else:
        return (tmp * tmp * n) % p

a = factorial_with_rest(n)
b = factorial_with_rest(k) * factorial_with_rest(n-k)

print(a * reduce(b, p-2) % p)
