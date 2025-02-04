import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque(enumerate(map(int, sys.stdin.readline().split())))
answers = []

while queue:
    idx, move = queue.popleft()
    answers.append(idx+1)

    if move > 0:
        queue.rotate(-(move-1))
    elif move < 0:
        queue.rotate(-move)
print(' '.join(map(str, answers)))