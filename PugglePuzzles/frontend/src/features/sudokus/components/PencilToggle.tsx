import { FC } from "react";
import useSudoku from "../hooks/useSudoku";

const PencilToggle: FC = () => {
  const { state: { usePencil }, actions: { toggleUsePencil }} = useSudoku()

  return (
    <div className="toggle-switch">
     
    </div>
  )
}
