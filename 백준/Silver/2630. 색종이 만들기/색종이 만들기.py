import sys
import math

def check_area(l, sa, sb):
    valueArr = [ boards[i][j] for j in range(sb, sb+l) for i in range(sa, sa+l) ]
    valueArr = list(set(valueArr))

    if len(valueArr) == 2:
        return -1
    else:
        return valueArr[0]


def split(l, sa, sb):
    global count_color, count_white
    if l == 1:
        if boards[sa][sb] == 1:
            count_color += 1
        else:
            count_white += 1
        return

    check_res = check_area(l, sa, sb)

    if check_res == 0:
        count_white += 1
        return
    elif check_res == 1:
        count_color += 1
        return

    split(l//2, sa, sb)
    split(l//2, sa+l//2, sb)
    split(l//2, sa, sb+l//2)
    split(l//2, sa+l//2, sb+l//2)

n = int(sys.stdin.readline())
boards = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]
count_white = 0
count_color = 0

split(n, 0, 0)

print(count_white)
print(count_color)
