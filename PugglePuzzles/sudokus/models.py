from django.db import models
from main.models import Puzzle
from sudokus.utils import generate
import json

class Sudoku(Puzzle):
    def create():
        sudoku_obj = generate()
        starting_grid = json.dump(sudoku_obj.starting_grid)
        solution = json.dump(sudoku_obj.solution)
        sudoku = Sudoku(starting_grid, solution)
        sudoku.save()
