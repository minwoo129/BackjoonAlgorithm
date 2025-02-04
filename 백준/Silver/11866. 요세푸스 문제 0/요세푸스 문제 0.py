import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

queue = deque([ i+1 for i in range(n) ])
answers = []
count = 1

while len(queue) != 0:
    popVal = queue.popleft()
    if count % k == 0:
        answers.append(popVal)
    else:
        queue.append(popVal)
    count += 1

print("<",", ".join(map(str, answers)),">", sep='')