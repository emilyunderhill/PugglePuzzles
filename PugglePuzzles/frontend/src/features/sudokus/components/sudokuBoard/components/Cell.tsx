import { FC } from "react";
import { SudokuCell } from "../../../redux/types";
import useSudoku from "../../../hooks/useSudoku";

export type CellProps = {
  cell: SudokuCell
  rowIndex: number
  colIndex: number
}

const Cell: FC<CellProps> = ({ cell, rowIndex, colIndex }) => {
  const { state: { selectedCellColIndex, selectedCellRowIndex }, actions: { selectCell }} = useSudoku()

  const getContent = () => {
    if (cell.value && cell.isFixed) {
      return <p className="fixed-value">{cell.value}</p>
    }

    if (cell.value) {
      return <p className="user-value">{cell.value}</p>
    }

    if (cell.possibleValues.length > 0) {
      return <div className="possible-values">
        {cell.possibleValues.map((value) => <p key={value} className="possible-value">{value}</p>)}
      </div>
    }
  }

  const handleSelectCell = () => {
    if (!cell.isFixed){
      selectCell({
        colIndex,
        rowIndex,
    })}
  }

  const isSelected = rowIndex === selectedCellRowIndex && colIndex === selectedCellColIndex

  return <div className={isSelected ? "sudoku-cell active-cell" : "sudoku-cell"} onClick={handleSelectCell}>
    {getContent()}
  </div>
}

export default Cell
