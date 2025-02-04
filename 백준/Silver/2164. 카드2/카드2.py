import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque([ i+1 for i in range(n) ])
popFlag = True

while len(queue) != 1:
    if popFlag:
        queue.popleft()
        popFlag = False
    else:
        val = queue.popleft()
        queue.append(val)
        popFlag = True

print(queue[0])