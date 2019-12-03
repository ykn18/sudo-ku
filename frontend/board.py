def isInRow(board, row, value):
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
    return True

