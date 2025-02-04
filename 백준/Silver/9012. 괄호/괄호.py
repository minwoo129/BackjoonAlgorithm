import sys

t = int(sys.stdin.readline())
answers = []
for _ in range(t):
    inputs = list(sys.stdin.readline().rstrip())
    stacks = []
    for val in inputs:
        if val == '(':
            stacks.append(val)
        else:
            if len(stacks) > 0:
                stacks.pop()
            else:
                answers.append('NO')
                break
    else:
        answers.append('YES' if len(stacks) == 0 else 'NO')

for val in answers:
    print(val)