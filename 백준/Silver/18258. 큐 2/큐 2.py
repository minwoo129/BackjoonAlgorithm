import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque([])
answers = []

for _ in range(n):
    inputVal = sys.stdin.readline().rstrip()

    if "push" in inputVal:
        orderType, num = inputVal.split()
        queue.append(int(num))
    elif "pop" in inputVal:
        if queue:
            answers.append(queue.popleft())
        else:
            answers.append(-1)
    elif "size" in inputVal:
        answers.append(len(queue))
    elif "empty" in inputVal:
        answers.append(0 if queue else 1)
    elif "front" in inputVal:
        if queue:
            answers.append(queue[0])
        else:
            answers.append(-1)
    elif "back" in inputVal:
        if queue:
            answers.append(queue[-1])
        else:
            answers.append(-1)

for val in answers:
    print(val)