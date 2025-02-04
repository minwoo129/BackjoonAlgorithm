import sys

n = int(sys.stdin.readline())
papers = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]

answers = [0, 0, 0]

def convertSplitArr(l, startx, starty):
    splitedArr = []

    endx = startx + l
    for i in range(l):
        splitedArr += papers[starty+i][startx:endx]
    return splitedArr

def findSolution(l, startx, starty):
    # 특정 시작 위치에 대해 NxN 크기 행렬의 요소 출력
    splitedArr = convertSplitArr(l, startx, starty)
    # splitedArr에서 중복요소 제거
    splitedSetArr = list(set(splitedArr[:]))

    # 행렬의 크기가 9인 경우(=행렬의 가로 또는 세로 크기가 3인 경우)
    # 이보다 작은 크기로는 더이상 쪼개질수 없음
    if l == 3:
        # 같은 수로만 되어있는 경우
        if len(splitedSetArr) == 1:
            val = splitedSetArr[0]
            answers[1+val] += 1
            return

        for val in splitedArr:
            answers[1+val] += 1
        return

    if len(splitedSetArr) == 1:
        val = splitedSetArr[0]
        answers[1+val] += 1
        return


    nextLen = l//3
    for i in range(9):
        newStartx = startx + nextLen * (i%3)
        newStarty = starty + nextLen * (i//3)

        findSolution(nextLen, newStartx, newStarty)

findSolution(n, 0, 0)

for val in answers:
    print(val)

