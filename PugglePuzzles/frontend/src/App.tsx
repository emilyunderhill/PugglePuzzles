import React from 'react';
import './App.css';
import { Routes, Route } from "react-router-dom";
import { ROUTE_SUDOKUS } from './library/routes';
import Sudokus from './features/sudokus';


function App() {
  return (
    <Routes>
      <Route path={ROUTE_SUDOKUS} Component={Sudokus} />
      <Route path='' Component={Sudokus} />
    </Routes>
  );
}

export default App;
