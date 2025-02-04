import sys, re

answers = []
def convertInputVal(inputVal):
    reg1 = r"[a-zA-Z.]"
    inputVal = re.sub(reg1, '', inputVal)
    inputVal = inputVal.replace(' ', '')

    return list(inputVal)
while True:
    inputVal = sys.stdin.readline().rstrip()
    stacks = []
    if inputVal[0] == '.':
        break

    vals = convertInputVal(inputVal)

    for val in vals:
        if val == '(' or val == '[':
            stacks.append(val)
        else:
            if val == ')':
                if len(stacks) == 0:
                    answers.append('no')
                    break
                if stacks[-1] == '(':
                    stacks.pop()
                    continue

                stacks.append(val)
            else:
                if len(stacks) == 0:
                    answers.append('no')
                    break
                if stacks[-1] == '[':
                    stacks.pop()
                    continue
                stacks.append(val)
    else:
        if len(stacks) == 0:
            answers.append('yes')
        else:
            answers.append('no')

for val in answers:
    print(val)