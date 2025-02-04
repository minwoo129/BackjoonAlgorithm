import sys

n = int(sys.stdin.readline())

def get_fibonacci(num):
    if num <= 1:
        return num

    return get_fibonacci(num-1) + get_fibonacci(num-2)

print(get_fibonacci(n))
