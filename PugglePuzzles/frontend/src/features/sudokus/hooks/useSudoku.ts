import { useAppDispatch, useAppSelector } from "../../../store"
import { SudokuState, deselectCell, selectCell, selectSudoku, selectSudokuState } from "../redux/sudokuSlice"

type SelectSudokuArg = {
  id: number,
  date: string
}

const useSudoku = () => {
  const state = useAppSelector(selectSudokuState) as SudokuState
  const dispatch = useAppDispatch()

  const handleSelectSudoku = (arg: SelectSudokuArg) => dispatch(selectSudoku(arg))
  const handleSelectCell = (arg: {rowIndex: number, colIndex: number}) => dispatch(selectCell(arg))
  const handleDeselectCell = () => dispatch(deselectCell())

  return {
    state,
    actions: {
      selectSudoku: handleSelectSudoku,
      selectCell: handleSelectCell,
      deselectCell: handleDeselectCell,
    }
  }
}

export default useSudoku
