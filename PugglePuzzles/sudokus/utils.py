import random
from functools import reduce

def generate():
    board = [[0 for _ in range(9)] for _ in range(9)]

    boardIsComplete = False

    while boardIsComplete == False:
        board = fillBoard(board)
        boardIsComplete = isBoardComplete(board)

    print(board)
    return board

def fillBoard(board: set) -> set:
    print('Filling board: ', board)
    for x in range(0,9):
        for y in range(0,9):
            if (board[x][y] > 0):
                continue

            val = getValidNumber(board, x, y)
            if (val == False):
                board = clearGridNums(board, x, y)
                val = getValidNumber(board, x, y)
            else:
                board[x][y] = val

    return board

def getValidNumber(board: set, row: int, col: int) -> int|bool:
    options = list(range(1, 10))
    random.shuffle(options)
    for x in options:
        if (isNumberValid(x, board, row, col)):
            return x
    return False

def isNumberValid(val: int, board: set, row: int, col: int) -> bool:
    if (val in board[row]):
        return False

    for rowX in board:
        if (rowX[col] == val):
            return False

    blockVals = getBlockVals(board, row, col)
    if (val in blockVals):
        return False

    return True


def getBlockVals(board: set, row: int, col: int) -> list:
    blockRows = getBlockGrid(row)
    blockCols = getBlockGrid(col)

    vals = []
    for blockRow in blockRows:
        for blockCol in blockCols:
            val = board[blockRow][blockCol]
            vals.append(val)

    return vals


def getBlockGrid(x:int) -> set:
    if (x < 3):
        return [0, 1, 2]

    if (x < 6):
        return [3, 4, 5]

    return [6, 7, 8]

def clearGridNums(board: set, row: int, col: int) -> set:
    board[row] = [0 for _ in range(9)]
    for x in range(0,9):
        board[x][col] = 0

    blockRows = getBlockGrid(row)
    blockCols = getBlockGrid(col)

    for blockRow in blockRows:
        for blockCol in blockCols:
            board[blockRow][blockCol] = 0

    return board

def isBoardComplete(board: set) -> bool:
    for x in range(0,9):
        for y in range(0,9):
            if (board[x][y] == 0):
                return False

    return True


if __name__ == "__main__":
    generate()
