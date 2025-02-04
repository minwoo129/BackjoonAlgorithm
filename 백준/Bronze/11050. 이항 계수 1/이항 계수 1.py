import sys
import math

n, k = map(int, sys.stdin.readline().split())

a = math.factorial(n)
b = math.factorial(n-k)*math.factorial(k)

answer = a // b

print(answer)