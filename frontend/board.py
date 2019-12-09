'''def isInRow(board, row, value):
    for col in range(9):
        if board[row][col] == value:
            return True
    return False

def isInCol(board, col, value):
    for row in range(9):
        if board[row][col] == value:
            return True
    return False

def isInSquare(board, row, col, value):
    row_start = row - (row % 3)
    col_start = col - (col % 3)
    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if board[i][j] == value:
                return True
    return False

def isLegal(board, row, col, value):
    if isInRow(board,row,value) or isInCol(board,col,value) or isInSquare(board,row,col,value):
        return False
    else:
        return True

def isDone(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0 or isLegal(board,i,j,board[i][j]) == False:
                print("is done ", False)
                return False
    print("is done ", True)
    return True'''

def verify(board, r, c, old, new, mask):
    for i in range(9):
        if board[i][c] == old or board[i][c] == new:
            mask[i][c] = True
        if board[r][i] == old or board[r][i] == new:
            mask[r][i] = True
    row_start = r - (r % 3)
    col_start = c - (c % 3)
    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if board[i][j] == old or board[i][j] == new:
                mask[i][j] = True
    verifyRow(board, r, mask)
    verifyCol(board, c, mask)
    verifySquare(board, r, c, mask)

def verifyCol(board, c, mask):
    nums = {}
    for i in range(9):
        if board[i][c] == 0:
            continue
        if not nums.get(board[i][c]):
            nums[board[i][c]] = [i]
        else:
            nums[board[i][c]].append(i)
    for k in nums.keys():
        if len(nums[k]) > 1:
            for j in nums[k]:
                mask[j][c] = False

def verifyRow(board, r, mask):
    nums = {}
    for i in range(9):
        if board[r][i] == 0:
            continue
        if not nums.get(board[r][i]):
            nums[board[r][i]] = [i]
        else:
            nums[board[r][i]].append(i)
    for k in nums.keys():
        if len(nums[k]) > 1:
            for j in nums[k]:
                mask[r][j] = False


def verifySquare(board, r, c, mask):
    row_start = r - (r % 3)
    col_start = c - (c % 3)
    nums = {}
    
    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if board[i][j] == 0:
                continue
            if not nums.get(board[i][j]):
                nums[board[i][j]] = [(i, j)]
            else:
                nums[board[i][j]].append((i, j))
    for k in nums.keys():
        if len(nums[k]) > 1:
            for t in nums[k]:
                mask[t[0]][t[1]] = False
