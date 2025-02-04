import sys

def hanoi(cnt, start, end):
    if cnt == 1:
        print(start, end)
        return

    hanoi(cnt-1, start, 6-start-end)
    print(start, end)
    hanoi(cnt-1, 6-start-end, end)

n = int(sys.stdin.readline())
print(2**n-1)
hanoi(n, 1, 3)
