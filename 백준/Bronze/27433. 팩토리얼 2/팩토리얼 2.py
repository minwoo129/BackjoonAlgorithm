import sys

n = int(sys.stdin.readline())

def get_factorial(res, num):
    if num == n:
        return res

    return get_factorial(res * (num+1), num+1)

if n == 0:
    print(1)
else:
    print(get_factorial(1, 1))