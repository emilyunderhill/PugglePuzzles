import { useAppDispatch, useAppSelector } from "../../../store"
import { useSaveProgressMutation } from "../redux/sudokuApi"
import { SudokuState, deselectCell, moveDown, moveLeft, moveRight, moveUp, onChangeValue, onClearCell, selectCell, selectSudoku, selectSudokuState, toggleUsePencil } from "../redux/sudokuSlice"

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
  const handleToggleUsePencil = () => dispatch(toggleUsePencil())
  const handleMoveLeft = () => dispatch(moveLeft())
  const handleMoveRight = () => dispatch(moveRight())
  const handleMoveUp = () => dispatch(moveUp())
  const handleMoveDown = () => dispatch(moveDown())
  const handleOnChangeValue = (val: number) => dispatch(onChangeValue(val))
  const handleOnClearCell = () => dispatch(onClearCell())

  return {
    state,
    actions: {
      selectSudoku: handleSelectSudoku,
      selectCell: handleSelectCell,
      deselectCell: handleDeselectCell,
      toggleUsePencil: handleToggleUsePencil,
      moveLeft: handleMoveLeft,
      moveRight: handleMoveRight,
      moveUp: handleMoveUp,
      moveDown: handleMoveDown,
      onChangeValue: handleOnChangeValue,
      onClearCell: handleOnClearCell,
    }
  }
}

export default useSudoku
