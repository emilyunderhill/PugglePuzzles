import random
import copy

class Cell:
    value: int = 0
    possibleValues: list = []

def generate():
    board: list[list[Cell]] = [[Cell() for _ in range(9)] for _ in range(9)]

    boardIsComplete = False

    while boardIsComplete == False:
        fillBoard(board)
        boardIsComplete = isBoardComplete(board)

    solutionValues = [[cell.value for cell in row] for row in board]

    initialBoard = removeNumbers(board)
    initialValues = [[cell.value for cell in row] for row in initialBoard]
    print('Initial values: ', initialValues)
    print('Solution values: ', solutionValues)

def fillBoard(board: list[list[Cell]]) -> None:
    for x in range(9):
        for y in range(9):
            if (board[x][y].value > 0):
                continue

            val = getValidNumber(board, x, y)
            if (not val):
                clearGridNums(board, x, y)
                val = getValidNumber(board, x, y)
            else:
                board[x][y].value = val

def getValidNumber(board: list[list[Cell]], row: int, col: int) -> int|bool:
    options = list(range(1, 10))
    random.shuffle(options)
    for x in options:
        if (isNumberValid(x, board, row, col)):
            return x
    return False

def isNumberValid(val: int, board: list[list[Cell]], row: int, col: int) -> bool:
    rowVals = [cell.value for cell in board[row]]
    if (val in rowVals):
        return False

    colVals = map(lambda rowX: rowX[col].value, board)
    if (val in colVals):
        return False

    blockVals = getBlockVals(board, row, col)
    if (val in blockVals):
        return False

    return True


def getBlockVals(board: list[list[Cell]], row: int, col: int) -> list[int]:
    blockRows = getBlockGrid(row)
    blockCols = getBlockGrid(col)

    vals = []
    for blockRow in blockRows:
        for blockCol in blockCols:
            val = board[blockRow][blockCol].value
            vals.append(val)

    return vals


def getBlockGrid(x: int) -> list[int]:
    if (x < 3):
        return [0, 1, 2]

    if (x < 6):
        return [3, 4, 5]

    return [6, 7, 8]

def clearGridNums(board: list[list[Cell]], row: int, col: int) -> None:
    board[row] = [Cell() for _ in range(9)]
    for x in range(9):
        board[x][col].value = 0

    blockRows = getBlockGrid(row)
    blockCols = getBlockGrid(col)

    for blockRow in blockRows:
        for blockCol in blockCols:
            board[blockRow][blockCol].value = 0


def isBoardComplete(board: list[list[Cell]]) -> bool:
    for x in range(9):
        for y in range(9):
            if (board[x][y].value == 0):
                return False

    return True

def removeNumbers(solutionBoard: list[list[Cell]]) -> list[list[Cell]]:
    newBoard = copy.deepcopy(solutionBoard)
    failedAttempt = 0

    while failedAttempt < 5:
        tempBoard = removeRandomNumber(newBoard)
        if (isBoardSolvable(tempBoard)):
            newBoard = copy.deepcopy(tempBoard)
        else:
            failedAttempt += 1

    return newBoard


def removeRandomNumber(board: list[list[Cell]]) -> list[list[Cell]]:
    val: int = 0

    while val == 0:
        row: int = random.randint(0,8)
        col: int = random.randint(0,8)
        val = board[row][col].value

    newBoard = copy.deepcopy(board)
    newBoard[row][col].value = 0

    return newBoard

def isBoardSolvable(board: list[list[Cell]]) -> bool:
    newBoard = copy.deepcopy(board)
    hasChanges = True

    retry = True

    while retry:
        hasChanges = False
        for x in range(9):
            for y in range(9):
                if (newBoard[x][y].value > 0):
                    continue

                possibleVals = findPossibleValues(newBoard, x, y)

                if possibleVals != newBoard[x][y].possibleValues:
                    newBoard[x][y].possibleValues = possibleVals
                    hasChanges = True

                if len(possibleVals) == 1:
                    newBoard[x][y].value = possibleVals[0]
                    hasChanges = True

                hasChanges = checkPossibleValues(newBoard, x, y, hasChanges)
        if not hasChanges:
            retry = False

    return isBoardComplete(newBoard)



def checkPossibleValues(board: list[list[Cell]], row: int, col: int, hasChanges: bool) -> bool:
    possibleValues = board[row][col].possibleValues
    # Check row
    duplicatePossibleValues = []
    i = 0
    for cell in board[row]:
        if (i == col):
            i += 1
            continue

        if (cell.possibleValues == possibleValues):
            duplicatePossibleValues.append(i)

        i += 1

    if (len(possibleValues) == len(duplicatePossibleValues)):
        i = 0
        for cell in board[row]:
            if (i in duplicatePossibleValues):
                i += 1
                continue

            for possibleVal in possibleValues:
                if (possibleVal in cell.possibleValues):
                    cell.possibleValues.remove(possibleVal)
                    hasChanges = True
                    if (len(cell.possibleValues) == 1):
                        cell.value = cell.possibleValues[0]

    return hasChanges


def findPossibleValues(board: set, row: int, col: int) -> list:
    possibleVals = []
    for x in range(1,10):
        if (isNumberValid(x, board, row, col)):
            possibleVals.append(x)

    return possibleVals

if __name__ == "__main__":
    generate()
