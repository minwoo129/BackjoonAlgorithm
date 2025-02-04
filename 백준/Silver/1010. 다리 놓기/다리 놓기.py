import sys
from math import factorial

t = int(sys.stdin.readline())
answers = []

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())

    a = factorial(m)
    b = factorial(m-n)*factorial(n)

    if b == 0:
        answers.append(1)
        continue

    answers.append(a // b)

print('\n'.join(map(str, answers)))