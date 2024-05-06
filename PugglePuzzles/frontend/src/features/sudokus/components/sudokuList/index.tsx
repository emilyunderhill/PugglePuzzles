import React, { FC } from "react";
import { useListSudokusQuery } from "../../redux/sudokuApi";

const SudokuList: FC = () => {
  const { data, isLoading, isError } = useListSudokusQuery({});

  if (isLoading) {
    return <div>Loading Sudoku list</div>
  }

  if (isError) {
    return <div>Error</div>
  }

  if (!data) {
    return null
  }


  return <div>
    {data.map((listItem) => {
      return <div key={listItem.id}>
        <p>Id: {listItem.id}</p>
        <p>date: {listItem.date}</p>
      </div>
    })}
  </div>
}

export default SudokuList
