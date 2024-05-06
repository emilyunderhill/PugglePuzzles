import { createSlice } from "@reduxjs/toolkit"
import { RootState } from "../../../store"

export type SudokuState = {
  selectedDate: null | string
  selectedId: null | number
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
    }
  }
})

export default sudokuSlice.reducer

export const { selectSudoku } = sudokuSlice.actions

export const selectSudokuState = (state: RootState) => state[name] as SudokuState
