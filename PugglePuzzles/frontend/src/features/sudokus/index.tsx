import { FC } from "react";
import SudokuList from "./components/sudokuList";
import "./style.scss";
import PageContainer from "../../components/PageContainer";

const Sudokus: FC = () => {
  return <PageContainer>
    <SudokuList />
  </PageContainer>
}

export default Sudokus
