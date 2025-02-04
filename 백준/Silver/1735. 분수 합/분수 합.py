import sys

a1, b1 = map(int, sys.stdin.readline().split())
a2, b2 = map(int, sys.stdin.readline().split())

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

lcd = (b1 * b2) // gcd(b1, b2)
mul1 = lcd // b1
mul2 = lcd // b2

a = a1 * mul1 + a2 * mul2
b = lcd

after_gcd = gcd(a, b)
a = a // after_gcd
b = b // after_gcd

print(str(a) + ' ' + str(b))
