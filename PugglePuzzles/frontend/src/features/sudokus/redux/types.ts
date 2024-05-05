export type SudokuListItem = {
  id: number,
  solved: boolean,
  inProgress: boolean,
}

export type SudokuList = SudokuListItem[]

export type SudokuCell = {
  value: number | null,
  isFixed: boolean,
  possibleValues: number[],
}

export type SudokuGridRow = SudokuCell[]
export type SudokuGrid = SudokuGridRow[]

export type GetArg = {
  id: number
}

export type SudokuGridRequest = {
  id: number,
  board: SudokuGrid
}

export type SudokuGridResponse = SudokuGridRequest

export type CellError = {
  rowIndex: number,
  colIndex: number
}

export type CheckGridResponse = {
  errors: CellError[]
}
