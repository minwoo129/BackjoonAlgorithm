import sys

def cut(a, n):
    if n == 1:
        return

    for i in range(a + n//3, a + (n//3)*2):
        result[i] = ' '
    cut(a, n//3)
    cut(a + (n//3)*2, n//3)


while True:
    try:
        n = int(sys.stdin.readline())
        result = ['-']*(3**n)
        cut(0, 3**n)
        print(''.join(map(str, result)))
    except:
        break
