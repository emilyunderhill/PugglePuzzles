import { FC } from "react";
import { SudokuListItem as SudokuListItemType } from "../../../redux/types";
import useSudoku from "../../../hooks/useSudoku";

type Props = {
  listItem: SudokuListItemType
}

const SudokuListItem: FC<Props> = ({ listItem }) => {
  const { state: { selectedId }, actions: { selectSudoku } } = useSudoku()

  const handleSelectSudoku = () => {
    selectSudoku({
      id: listItem.id,
      date: listItem.date
    })
  }

  const getClassName = () => {
    const className = 'sudoku-list-item'
    if (listItem.id === selectedId) {
      return className + ' selected'
    }

    if (listItem.solved) {
      return className + ' solved'
    }

    if (listItem.inProgress) {
      return className + ' in-progress'
    }

    return className
  }

  return <div className={getClassName()} onClick={handleSelectSudoku}>
    {listItem.date}
  </div>
}

export default SudokuListItem
