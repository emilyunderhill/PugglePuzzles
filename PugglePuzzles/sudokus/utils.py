import random
import copy

class Cell:
    value: int = 0
    possible_values: list = []

class SudokuObj:
    solution: list[list[int]]
    starting_grid: list[list[int]]

    def __init__(self, solution, starting_grid):
        self.solution = solution
        self.starting_grid = starting_grid

def generate():
    board: list[list[Cell]] = [[Cell() for _ in range(9)] for _ in range(9)]

    board_is_complete = False

    while not board_is_complete:
        fill_board(board)
        board_is_complete = is_board_complete(board)

    solution_values = [[cell.value for cell in row] for row in board]

    initial_board = remove_numbers(board)
    initial_values = [[cell.value for cell in row] for row in initial_board]

    sudoku_obj = SudokuObj(solution=solution_values, starting_grid=initial_values)

    return sudoku_obj

def fill_board(board: list[list[Cell]]) -> None:
    for x in range(9):
        for y in range(9):
            if (board[x][y].value > 0):
                continue

            val = get_valid_value(board, x, y)
            if (not val):
                clear_grid_for_retry(board, x, y)
                val = get_valid_value(board, x, y)
            else:
                board[x][y].value = val

def get_valid_value(board: list[list[Cell]], row: int, col: int) -> int|bool:
    options = list(range(1, 10))
    random.shuffle(options)
    for x in options:
        if (is_value_valid(x, board, row, col)):
            return x
    return False

def is_value_valid(val: int, board: list[list[Cell]], row: int, col: int) -> bool:
    row_values = [cell.value for cell in board[row]]
    if (val in row_values):
        return False

    col_values = map(lambda r: r[col].value, board)
    if (val in col_values):
        return False

    block_values = get_block_values(board, row, col)
    if (val in block_values):
        return False

    return True


def get_block_values(board: list[list[Cell]], row: int, col: int) -> list[int]:
    block_rows = get_block_grid(row)
    block_cols = get_block_grid(col)

    vals = []
    for block_row in block_rows:
        for block_col in block_cols:
            val = board[block_row][block_col].value
            vals.append(val)

    return vals


def get_block_grid(x: int) -> list[int]:
    if (x < 3):
        return [0, 1, 2]

    if (x < 6):
        return [3, 4, 5]

    return [6, 7, 8]

def clear_grid_for_retry(board: list[list[Cell]], row: int, col: int) -> None:
    board[row] = [Cell() for _ in range(9)]
    for x in range(9):
        board[x][col].value = 0

    block_rows = get_block_grid(row)
    block_cols = get_block_grid(col)

    for block_row in block_rows:
        for block_col in block_cols:
            board[block_row][block_col].value = 0


def is_board_complete(board: list[list[Cell]]) -> bool:
    for x in range(9):
        for y in range(9):
            if (board[x][y].value == 0):
                return False

    return True

def remove_numbers(solution_board: list[list[Cell]]) -> list[list[Cell]]:
    new_board = copy.deepcopy(solution_board)
    failed_attempt = 0

    while failed_attempt < 81:
        temp_board = remove_random_value(new_board)
        if (is_board_solvable(temp_board)):
            new_board = copy.deepcopy(temp_board)
        else:
            failed_attempt += 1

    return new_board


def remove_random_value(board: list[list[Cell]]) -> list[list[Cell]]:
    val: int = 0

    while val == 0:
        row: int = random.randint(0,8)
        col: int = random.randint(0,8)
        val = board[row][col].value

    new_board = copy.deepcopy(board)
    new_board[row][col].value = 0

    return new_board

def is_board_solvable(board: list[list[Cell]]) -> bool:
    new_board = copy.deepcopy(board)
    has_changes = True

    retry = True

    while retry:
        has_changes = False
        for x in range(9):
            for y in range(9):
                if (new_board[x][y].value > 0):
                    continue

                possible_values = find_possible_values(new_board, x, y)

                if possible_values != new_board[x][y].possible_values:
                    new_board[x][y].possible_values = possible_values
                    has_changes = True

                if len(possible_values) == 1:
                    new_board[x][y].value = possible_values[0]
                    has_changes = True

                has_changes = check_possible_values(new_board, x, y, has_changes)
        if not has_changes:
            retry = False

    return is_board_complete(new_board)

def find_possible_values(board: set, row: int, col: int) -> list:
    possible_values = []
    for x in range(1,10):
        if (is_value_valid(x, board, row, col)):
            possible_values.append(x)

    return possible_values

def check_possible_values(board: list[list[Cell]], row: int, col: int, has_changes: bool) -> bool:
    current_cell = board[row][col]
    # Check row
    row_cells = board[row]
    has_changes = check_for_values_not_in_other_cells(row_cells, current_cell, has_changes)
    has_changes = check_for_cells_with_the_same_possible_numbers(row_cells, current_cell, has_changes)

    # Check col
    col_cells = list(row[col] for row in board)
    has_changes = check_for_values_not_in_other_cells(col_cells, current_cell, has_changes)
    has_changes = check_for_cells_with_the_same_possible_numbers(col_cells, current_cell, has_changes)

    # Check block
    block_rows = get_block_grid(row)
    block_cols = get_block_grid(col)
    block_cells = []
    for block_row in block_rows:
        for block_col in block_cols:
            block_cells.append(board[block_row][block_col])
    has_changes = check_for_values_not_in_other_cells(block_cells, current_cell, has_changes)
    has_changes = check_for_cells_with_the_same_possible_numbers(block_cells, current_cell, has_changes)

    return has_changes


def check_for_values_not_in_other_cells(cells: list[Cell], current_cell: Cell, has_changes: bool) -> bool:
    # If a possible value is not possible in any other cell, we know it must be the value of this cell
    possible_values = current_cell.possible_values

    for possible_value in possible_values:
        possible_cells = list(filter(lambda c: possible_value in c.possible_values, cells))

        if (len(possible_cells) == 1):
            current_cell.value = possible_value
            current_cell.possible_values = [possible_value]
            has_changes = True

    return has_changes

def check_for_cells_with_the_same_possible_numbers(cells: list[Cell], current_cell: Cell, has_changes: bool) -> bool:
    # If the same numbers are the only possible numbers in the same cells then we know that the numbers cannot exist in any other cell
    # Ie if col 1 and col 2 only have the possible numbers 1 & 2, then we know 1 & 2 cannot exist elsewhere in the row.
    possible_values = current_cell.possible_values
    duplicate_indexes = []
    i = 0
    for cell in cells:
        if (cell.possible_values == possible_values):
            duplicate_indexes.append(i)
        i += 1

    if (len(possible_values) > 0 and len(possible_values) == len(duplicate_indexes)):
        i = -1
        for cell in cells:
            i += 1
            if (i in duplicate_indexes):
                continue

            # Remove the possible values from other cells
            for possible_value in possible_values:
                if (possible_value in cell.possible_values):
                    cell.possible_values.remove(possible_value)
                    has_changes = True
                    if (len(cell.possible_values) == 1):
                        cell.value = cell.possible_values[0]
    return has_changes

if __name__ == "__main__":
    generate()
