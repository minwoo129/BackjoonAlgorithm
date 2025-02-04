import sys

n = int(sys.stdin.readline())
answer = []

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    lcd = a * b // gcd(a, b)
    answer.append(lcd)

print('\n'.join(map(str, answer)))
