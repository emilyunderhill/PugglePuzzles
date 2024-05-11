import React, { FC } from "react"
import useSudoku from "../../hooks/useSudoku"
import { useGetSudokuQuery } from "../../redux/sudokuApi"
import Cell, { CellProps } from "./components/Cell"
import Block, { BlockProps } from "./components/Block"

const SudokuBoard: FC = () => {
  const { state: { selectedDate, board }} = useSudoku()
  const { isLoading, isError } = useGetSudokuQuery({ date: selectedDate })

  if (isLoading) {
    return <div>
      Loading
    </div>
  }

  if (isError){
    return <div>
      Error
    </div>
  }

  const getBlocks = () => {
    const blocks = [[], [], [], [], [], [], [], [], []] as CellProps[][]
    for (let rowI = 0; rowI < 9; rowI ++) {
      const row = board[rowI]
      for (let colI = 0; colI < 9; colI ++) {
        const cell = row[colI]

        const cellProps = {
              cell,
              rowIndex: rowI,
              colIndex: colI
            }

        if (rowI < 3) {
          if (colI < 3){
            blocks[0].push(cellProps)
            continue
          }

          if (colI < 6) {
            blocks[1].push(cellProps)
            continue
          }

          blocks[2].push(cellProps)
          continue
        }

        if (rowI < 6) {
          if (colI < 3){
            blocks[3].push(cellProps)
            continue
          }

          if (colI < 6) {
            blocks[4].push(cellProps)
            continue
          }

          blocks[5].push(cellProps)
          continue
        }

        if (colI < 3){
            blocks[6].push(cellProps)
            continue
          }

          if (colI < 6) {
            blocks[7].push(cellProps)
            continue
          }

          blocks[8].push(cellProps)
      }
    }

    return blocks
  }

  return <div className="sudoku-board">
    {getBlocks().map((block) => <Block cells={block} />)}
  </div>
}

export default SudokuBoard
