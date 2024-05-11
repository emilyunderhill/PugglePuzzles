import { useAppDispatch, useAppSelector } from "../../../store"
import { SudokuState, clearCellPossibleValues as clearCellPossibleValues, deselectCell, moveDown, moveLeft, moveRight, moveUp, removeCellValue, selectCell, selectSudoku, selectSudokuState, setCellValue, toggleCellPossibleValue, toggleUsePencil } from "../redux/sudokuSlice"

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
  const handleSetCellValue = (val: number) => dispatch(setCellValue(val))
  const handleRemoveCellValue = () => dispatch(removeCellValue())
  const handleToggleCellPossibleValue = (val: number) => dispatch(toggleCellPossibleValue(val))
  const handleClearCellPossibleValues = () => dispatch(clearCellPossibleValues())
  const handleMoveLeft = () => dispatch(moveLeft())
  const handleMoveRight = () => dispatch(moveRight())
  const handleMoveUp = () => dispatch(moveUp())
  const handleMoveDown = () => dispatch(moveDown())

  return {
    state,
    actions: {
      selectSudoku: handleSelectSudoku,
      selectCell: handleSelectCell,
      deselectCell: handleDeselectCell,
      toggleUsePencil: handleToggleUsePencil,
      setCellValue: handleSetCellValue,
      removeCellValue: handleRemoveCellValue,
      toggleCellPossibleValue: handleToggleCellPossibleValue,
      clearCellPossibleValues: handleClearCellPossibleValues,
      moveLeft: handleMoveLeft,
      moveRight: handleMoveRight,
      moveUp: handleMoveUp,
      moveDown: handleMoveDown,
    }
  }
}

export default useSudoku
