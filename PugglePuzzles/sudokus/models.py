from django.db import models
from sudokus.utils import generate
from main.models import IPAddressUser
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

class UserSudoku(models.Model):
    user = models.ForeignKey(
        IPAddressUser,
        on_delete=models.CASCADE,
    )
    sudoku = models.ForeignKey(
        Sudoku,
        on_delete=models.CASCADE
    )
    completed = models.BooleanField(
        default=False
    )
    start = models.DateTimeField(
        auto_now=True
    )
    duration = models.BigIntegerField(
        default=0
    )
    hints_count = models.IntegerField(
        default=0
    )
    progress = models.CharField(
        max_length=300,
        null=True
    )
