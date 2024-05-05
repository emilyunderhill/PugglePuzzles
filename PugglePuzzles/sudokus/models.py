from django.db import models
from sudokus.utils import generate
import json

class Sudoku(models.Model):
    start = models.CharField(max_length=300, default="[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]")
    solution = models.CharField(max_length=300, default="[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]")

    def create():
        sudoku_obj = generate()
        sudoku = Sudoku()
        start_string = json.dumps(sudoku_obj.starting_grid)
        solution_string = json.dumps(sudoku_obj.solution)
        sudoku.start = start_string
        sudoku.solution = solution_string
        sudoku.save()
