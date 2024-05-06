from django.db import models
from sudokus.utils import generate
from main.models import IPAddressUser
import json, datetime

class SudokuManager(models.Manager):
    def find_or_create_by_date(self, date: datetime.date) -> 'Sudoku':
        if (not self.filter(date=date).exists()):
            Sudoku.create(date.strftime("%d-%m-%Y"))

        return self.get(date=date)

    def find_all_by_date(self, date: datetime.date) -> list['Sudoku']:
        month = date.month

        return self.filter(date__month=month).order_by('-date')

class Sudoku(models.Model):
    start = models.CharField(max_length=300, default="[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]")
    solution = models.CharField(max_length=300, default="[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]")
    date = models.DateField(null=True, default=None)

    objects = SudokuManager()

    def create(date_str: str):
        date = datetime.datetime.strptime(date_str, "%d-%m-%Y").date()

        sudoku_obj = generate()
        sudoku = Sudoku()
        start_string = json.dumps(sudoku_obj.starting_grid)
        solution_string = json.dumps(sudoku_obj.solution)
        sudoku.start = start_string
        sudoku.solution = solution_string
        sudoku.date = date
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
