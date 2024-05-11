import { createSlice } from "@reduxjs/toolkit"
import { RootState, store } from "../../../store"
import { CellError, SudokuGrid } from "./types"
import { sudokusApi } from "./sudokuApi"

export type SudokuState = {
  selectedDate: null | string
  selectedId: null | number
  selectedCellRowIndex: null | number
  selectedCellColIndex: null | number
  usePencil: boolean
  board: SudokuGrid
  errors: CellError[]
}

export const name = 'SelectedSudoku'

const getInitialBoard = (): SudokuGrid => {
  const board = [];
  for (let row = 0; row < 9; row ++) {
    const cols = []
    for (let col = 0; col < 9; col ++) {
      cols.push({
        value: 0,
        isFixed: false,
        possibleValues: [],
      })
    }
    board.push(cols)
  }
  return board
}

const sudokuSlice = createSlice({
  name,
  initialState: {
    selectedDate: null,
    selectedId: null,
    selectedCellColIndex: null,
    selectedCellRowIndex: null,
    usePencil: false,
    board: getInitialBoard(),
    errors: [],
  } as SudokuState,
  reducers: {
    selectSudoku: (state, action) => {
      state.selectedDate = action.payload.date
      state.selectedId = action.payload.id
    },
    selectCell: (state, action) => {
      state.selectedCellRowIndex = action.payload.rowIndex
      state.selectedCellColIndex = action.payload.colIndex
    },
    deselectCell: (state) => {
      state.selectedCellColIndex = null
      state.selectedCellRowIndex = null
    },
    toggleUsePencil: (state) => {
      state.usePencil = !state.usePencil
    },
    setCellValue: (state, action) => {
      if (state.selectedCellRowIndex === null || state.selectedCellColIndex === null) {
        return
      }
      state.board[state.selectedCellRowIndex][state.selectedCellColIndex].value = action.payload
    },
    removeCellValue: (state) => {
      if (!state.selectedCellRowIndex || !state.selectedCellColIndex) {
        return
      }
      state.board[state.selectedCellRowIndex][state.selectedCellColIndex].value = 0
    },
    toggleCellPossibleValue: (state, action) => {
      if (state.selectedCellRowIndex === null || state.selectedCellColIndex === null) {
        return
      }
      const possibleValues = state.board[state.selectedCellRowIndex][state.selectedCellColIndex].possibleValues
      const possibleValue = action.payload
      const index = possibleValues.findIndex((value) => value === possibleValue)

      if (index < 0){
        state.board[state.selectedCellRowIndex][state.selectedCellColIndex].possibleValues.push(possibleValue)
        return
      }

      state.board[state.selectedCellRowIndex][state.selectedCellColIndex].possibleValues.splice(index, 1)
    },
    clearCellPossibleValues: (state) => {
      if (state.selectedCellRowIndex === null || state.selectedCellColIndex === null) {
        return
      }
      state.board[state.selectedCellRowIndex][state.selectedCellColIndex].possibleValues = []
    },
    moveLeft: (state) => {
      if (state.selectedCellRowIndex === null || state.selectedCellColIndex === null) {
        return
      }
      const currentColIndex = state.selectedCellColIndex
      state.selectedCellColIndex = currentColIndex === 0 ? 8 : currentColIndex - 1
    },
    moveRight: (state) => {
      if (state.selectedCellRowIndex === null || state.selectedCellColIndex === null) {
        return
      }
      const currentColIndex = state.selectedCellColIndex
      state.selectedCellColIndex = currentColIndex === 8 ? 0 : currentColIndex + 1
    },
    moveUp: (state) => {
      if (state.selectedCellRowIndex === null || state.selectedCellColIndex === null) {
        return
      }
      const currentRowIndex = state.selectedCellRowIndex
      state.selectedCellRowIndex = currentRowIndex === 0 ? 8 : currentRowIndex - 1
    },
    moveDown: (state) => {
      if (state.selectedCellRowIndex === null || state.selectedCellColIndex === null) {
        return
      }
      const currentRowIndex = state.selectedCellRowIndex
      state.selectedCellRowIndex = currentRowIndex === 8 ? 0 : currentRowIndex + 1
    }
  },
  extraReducers: (builder) => {
    builder.addMatcher(sudokusApi.endpoints.getSudoku.matchFulfilled, (state, action) => {
      const boardResponse = action.payload.board
      state.board = [...boardResponse]
    })
  }
})

export default sudokuSlice.reducer

export const {
  selectSudoku,
  selectCell,
  deselectCell,
  toggleUsePencil,
  setCellValue,
  removeCellValue,
  toggleCellPossibleValue,
  clearCellPossibleValues,
  moveLeft,
  moveRight,
  moveUp,
  moveDown,
} = sudokuSlice.actions

export const selectSudokuState = (state: RootState) => state[name] as SudokuState
