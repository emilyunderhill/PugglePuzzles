import { FC, useEffect } from "react"
import SudokuList from "./components/sudokuList"
import "./style.scss"
import PageContainer from "../../components/PageContainer"
import SudokuBoard from "./components/sudokuBoard"
import useSudoku from "./hooks/useSudoku"

const Sudokus: FC = () => {
  const {
    state: {
      selectedCellColIndex,
      selectedCellRowIndex,
      usePencil,
    },
    actions: {
      clearCellPossibleValues,
      removeCellValue,
      setCellValue,
      toggleCellPossibleValue,
      moveDown,
      moveLeft,
      moveRight,
      moveUp,
      toggleUsePencil,
    }
  } = useSudoku()

  useEffect(() => {
    document.addEventListener('keydown', handleOnKeyDown)
  }, [])

  const handleOnKeyDown = (event: KeyboardEvent) => {
    const key = event.key
    console.log({key})
    switch (key) {
        case 'Backspace':
        case 'Delete':
          usePencil ? clearCellPossibleValues() : removeCellValue()
          return
        case 'ArrowLeft':
          moveLeft()
          return
        case 'ArrowRight':
          moveRight()
          return
        case 'ArrowUp':
          moveUp()
          return
        case 'ArrowDown':
          moveDown()
          return
        case 'p':
          toggleUsePencil()
          return
        default:
          if (isNaN(Number(key))) {
            return
          }
          usePencil ? toggleCellPossibleValue(Number(key)) : setCellValue(Number(key))
      }
  }

  return (
    <PageContainer>
        <SudokuList />
        <SudokuBoard />
    </PageContainer>
  )
}

export default Sudokus
