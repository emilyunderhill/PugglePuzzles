import { FC } from "react";
import SudokuList from "./components/sudokuList";
import "./style.scss";
import PageContainer from "../../components/PageContainer";
import SudokuBoard from "./components/sudokuBoard";

const Sudokus: FC = () => {
  return <PageContainer>
    <SudokuList />
    <SudokuBoard />
  </PageContainer>
}

export default Sudokus
