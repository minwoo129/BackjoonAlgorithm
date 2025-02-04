import sys, math

n = int(sys.stdin.readline())
stack = []
answers = []

for i in range(n):
    inputVal = sys.stdin.readline().rstrip()
    if inputVal[0] == "1":
        order, val = map(int, inputVal.split())
        stack.append(val)
        continue
    if inputVal[0] == "2":
        if len(stack) > 0:
            answers.append(stack.pop())
        else:
            answers.append(-1)
        continue
    if inputVal[0] == "3":
        answers.append(len(stack))
        continue
    if inputVal[0] == "4":
        answers.append(1 if len(stack) == 0 else 0)
        continue
    if inputVal[0] == "5":
        if len(stack) > 0:
            answers.append(stack[-1])
        else:
            answers.append(-1)

for val in answers:
    print(val)
