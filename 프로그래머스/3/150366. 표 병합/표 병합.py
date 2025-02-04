SIZE = 51
merged = [ [(i, j) for j in range(SIZE)] for i in range(SIZE) ]
board = [ ['EMPTY'] * SIZE for _ in range(SIZE) ]
answer = []

def UPDATE(r, c, value):
    x, y = merged[r][c]
    board[x][y] = value

def UPDATE_VALUE(value1, value2):
    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] == value1:
                board[i][j] = value2
                
def MERGE(r1, c1, r2, c2):
    if (r1, c1) == (r2, c2):
        return
    x1, y1 = merged[r1][c1]
    x2, y2 = merged[r2][c2]
    
    if board[x1][y1] == 'EMPTY':
        board[x1][y1] = board[x2][y2]
    
    for i in range(SIZE):
        for j in range(SIZE):
            if merged[i][j] == (x2, y2):
                merged[i][j] = (x1, y1)

def UNMERGE(r, c):
    x, y = merged[r][c]
    tmp = board[x][y]
    
    for i in range(SIZE):
        for j in range(SIZE):
            if merged[i][j] == (x, y):
                merged[i][j] = (i, j)
                board[i][j] = 'EMPTY'
    board[r][c] = tmp

def PRINT(r, c):
    x, y = merged[r][c]
    answer.append(board[x][y])

def solution(commands):
    
    for c in commands:
        order, *datas = c.split(' ')
        
        if order == 'UPDATE':
            if len(datas) == 3:
                r, c, value = int(datas[0]), int(datas[1]), datas[2]
                UPDATE(r, c, value)
            else:
                value1, value2 = datas[0], datas[1]
                UPDATE_VALUE(value1, value2)
                
        elif order == 'MERGE':
            r1, c1, r2, c2 = map(int, datas)
            MERGE(r1, c1, r2, c2)
        elif order == 'UNMERGE':
            r, c = map(int, datas)
            UNMERGE(r, c)
        else:
            r, c = map(int, datas)
            PRINT(r, c)
            
    return answer