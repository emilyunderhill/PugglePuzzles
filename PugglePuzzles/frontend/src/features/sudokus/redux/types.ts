export type SudokuListItem = {
  id: number
  solved: boolean
  inProgress: boolean
  date: string
}

export type SudokuList = SudokuListItem[]

export type SudokuCell = {
  value: number | null
  isFixed: boolean
  possibleValues: number[]
}

export type SudokuGridRow = SudokuCell[]
export type SudokuGrid = SudokuGridRow[]

export type GetGridArg = {
  date: string | null
}

export type GetListArg = GetGridArg

export type SudokuGridResponse = {
  id: number
  date: string
  board: SudokuGrid
}

export type CellError = {
  rowIndex: number
  colIndex: number
}

export type CheckGridRequest = {
  id: number
  board: SudokuGrid
}

export type CheckGridResponse = {
  id: number
  errors: CellError[]
}
