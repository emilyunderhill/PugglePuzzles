import { useAppDispatch, useAppSelector } from "../../../store"
import { SudokuState, selectSudoku, selectSudokuState } from "../redux/sudokuSlice"

type SelectSudokuArg = {
  id: number,
  date: string
}

const useSudoku = () => {
  const state = useAppSelector(selectSudokuState) as SudokuState
  const dispatch = useAppDispatch()

  const handleSelectSudoku = (arg: SelectSudokuArg) => dispatch(selectSudoku(arg))

  return {
    state: {
      selectedDate: state.selectedDate,
      selectedId: state.selectedId
    },
    actions: {
      selectSudoku: handleSelectSudoku
    }
  }
}

export default useSudoku
