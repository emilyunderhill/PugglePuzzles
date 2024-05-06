import { createSlice } from "@reduxjs/toolkit"
import { RootState } from "../../../store"

export type SudokuState = {
  selectedDate: null | string
  selectedId: null | number
  selectedCellRowIndex: null | number
  selectedCellColIndex: null | number
}

export const name = 'SelectedSudoku'

const sudokuSlice = createSlice({
  name,
  initialState: {
    selectedDate: null,
    selectedId: null,
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
    }
  }
})

export default sudokuSlice.reducer

export const { selectSudoku, selectCell, deselectCell } = sudokuSlice.actions

export const selectSudokuState = (state: RootState) => state[name] as SudokuState
