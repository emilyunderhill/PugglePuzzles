import { FC, useEffect, useState } from "react"
import SudokuList from "./components/sudokuList"
import "./style.scss"
import PageContainer from "../../components/PageContainer"
import SudokuBoard from "./components/sudokuBoard"
import useSudoku from "./hooks/useSudoku"
import { useSaveProgressMutation } from "./redux/sudokuApi"
import useDebounce from "../../hooks/useDebounce"

const Sudokus: FC = () => {
  const {
    state: {
      selectedId,
      board,
    },
    actions: {
      moveDown,
      moveLeft,
      moveRight,
      moveUp,
      toggleUsePencil,
      onChangeValue,
      onClearCell,
    }
  } = useSudoku()

  const [hasChanged, setHasChanged] = useState<boolean>(false)
  const debouncedHasChanged = useDebounce({ value: hasChanged, delay: 500})

  const [saveProgress] = useSaveProgressMutation()

  useEffect(() => {
    document.addEventListener('keydown', handleOnKeyDown)
    document.body.style.overflow = "hidden";
    return () => {
        document.body.style.overflow = "scroll"
    }
  }, [])

  useEffect(() => {
    if (!debouncedHasChanged || !selectedId) {
      return
    }

    saveProgress({id: selectedId, board})
    setHasChanged(false)
  }, [debouncedHasChanged])

  const handleOnKeyDown = (event: KeyboardEvent) => {
    const key = event.key
    switch (key) {
        case 'Backspace':
        case 'Delete':
          onClearCell()
          setHasChanged(true)
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
          if (isNaN(Number(key)) || key === '0') {
            return
          }
          onChangeValue(Number(key))
          setHasChanged(true)
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
