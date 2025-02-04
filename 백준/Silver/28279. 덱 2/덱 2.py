import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque([])
answers = []

for _ in range(n):
    inputval = sys.stdin.readline().rstrip()

    if inputval[0] == "1":
        order, val = inputval.split()
        queue.appendleft(int(val))
    elif inputval[0] == "2":
        order, val = inputval.split()
        queue.append(int(val))
    elif inputval[0] == "3":
        if queue:
            answers.append(queue.popleft())
        else:
            answers.append(-1)
    elif inputval[0] == "4":
        if queue:
            answers.append(queue.pop())
        else:
            answers.append(-1)
    elif inputval[0] == "5":
        answers.append(len(queue))
    elif inputval[0] == "6":
        answers.append(0 if queue else 1)
    elif inputval[0] == "7":
        if queue:
            answers.append(queue[0])
        else:
            answers.append(-1)
    else:
        if queue:
            answers.append(queue[-1])
        else:
            answers.append(-1)

for val in answers:
    print(val)