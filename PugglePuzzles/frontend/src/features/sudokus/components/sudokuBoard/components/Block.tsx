import { FC } from "react"
import { SudokuCell } from "../../../redux/types"
import Cell, { CellProps } from "./Cell"

export type BlockProps = {
  cells: CellProps[]
}

const Block: FC<BlockProps> = ({ cells }) => {
  return <div className="sudoku-block">
    {cells.map(({cell, colIndex, rowIndex}) => <Cell cell={cell} colIndex={colIndex} rowIndex={rowIndex} />)}
  </div>
}

export default Block
