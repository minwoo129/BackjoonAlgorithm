import sys

n = int(sys.stdin.readline())
video = [ list(sys.stdin.readline().rstrip()) for _ in range(n) ]

def splitArr(l, startx, starty):
    splitedArr = []

    endx = startx + l
    for i in range(l):
        splitedArr += video[starty+i][startx:endx]
    return splitedArr


def findSolution(l, startx, starty):
    treeArr = splitArr(l, startx, starty)
    treeSetArr = list(set(treeArr))

    if l == 2:
        if len(treeSetArr) == 1:
            return treeSetArr[0]
        else:
            return '(' + ''.join(treeArr) + ')'


    if len(treeSetArr) == 1:
        return treeSetArr[0]

    answer = '('
    answer += findSolution(l//2, startx, starty)
    if startx < n and starty < n:
        answer += findSolution(l//2, startx + l//2, starty)
        answer += findSolution(l//2, startx, starty+l//2)
        answer += findSolution(l//2, startx+l//2, starty+l//2)
    answer += ')'

    return answer

answer = findSolution(n, 0, 0)

print(answer)

