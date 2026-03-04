import sys
from math import sqrt

case = int(sys.stdin.readline())
answers = []

for _ in range(case):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    
    # 중심이 같은 원
    if x1 == x2 and y1 == y2:
        # 동심원(반지름까지 같은 경우)
        if r1 == r2:
            answers.append(-1)
        else:
            answers.append(0)
        continue
    
    # 중심이 다른 경우
    # 두 원의 중심사이의 거리
    centerLen = sqrt(((x1 - x2)**2) + ((y1 - y2)**2))
    
    # 작은 원이 큰 원 안에 있는 경우
    if centerLen < abs(r1 - r2):
        answers.append(0)
        continue
    # 작은 원이 큰 원 안에 있으면서 내접하는 경우
    if centerLen == abs(r1 - r2):
        answers.append(1)
        continue
    # 작은 원이 큰 원 밖으로 점점 벗어나는 경우
    if centerLen > abs(r1 - r2) and centerLen < (r1+r2):
        answers.append(2)
        continue
    # 작은 원이 큰 원과 밖에서 외접하는 경우
    if centerLen == (r1+r2):
        answers.append(1)
        continue
    
    answers.append(0)
print('\n'.join(map(str, answers)))