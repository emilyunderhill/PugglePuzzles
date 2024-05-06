import React, { FC } from "react";
import { useListSudokusQuery } from "../../redux/sudokuApi";
import useSudoku from "../../hooks/useSudoku";
import { type SudokuListItem as SudokuListItemType } from "../../redux/types";
import SudokuListItem from "./components/SudokuListItem";

const SudokuList: FC = () => {
  const { data, isLoading, isError } = useListSudokusQuery({ date: null })

  if (isLoading) {
    return <div>Loading Sudoku list</div>
  }

  if (isError) {
    return <div>Error</div>
  }

  if (!data) {
    return null
  }

  return <div className="grid-5">
    {data.map((listItem) => {
      return <SudokuListItem key={listItem.id} listItem={listItem} />
    })}
  </div>
}

export default SudokuList
