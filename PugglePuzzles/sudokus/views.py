from rest_framework.views import APIView
from django.http import HttpRequest, JsonResponse
from sudokus.models import Sudoku, UserSudoku
from main.models import IPAddressUser
from main.utils import get_ip_address_user_from_request
import json, datetime
from datetime import date

KEY_ID = 'id'
KEY_DATE = 'date'
KEY_BOARD = 'board'

class List(APIView):
    def get(self, request: HttpRequest) -> JsonResponse:
        user = get_ip_address_user_from_request(request)

        date_str = request.GET.get(KEY_DATE)
        if (not date_str):
            date = datetime.date.today()
        else:
            date = datetime.datetime.strptime(date_str, "%d-%m-%Y")


        sudokus: list[Sudoku] = Sudoku.objects.find_all_by_date(date)

        response = []
        for sudoku in sudokus:
            if (not UserSudoku.objects.filter(user=user.pk, sudoku=sudoku.pk).exists()):
                response.append({
                    'id': sudoku.pk,
                    'solved': False,
                    'inProgress': False,
                    'date': datetime.date.strftime(sudoku.date, "%d-%m-%Y")
                })
            else:
                user_sudoku = UserSudoku.objects.get(user=user.pk, sudoku=sudoku.pk)
                response.append({
                    'id': sudoku.pk,
                    'solved': user_sudoku.completed,
                    'inProgress': not user_sudoku.completed,
                    'date': datetime.date.strftime(sudoku.date, "%d-%m-%Y")
                })


        return JsonResponse(response, safe=False)

class Start(APIView):
    def get(self, request: HttpRequest) -> JsonResponse:
        user = get_ip_address_user_from_request(request)

        date_str = request.GET.get(KEY_DATE)
        if (not date_str):
            date = datetime.date.today()
        else:
            date = datetime.datetime.strptime(date_str, "%d-%m-%Y")

        sudoku: Sudoku = Sudoku.objects.find_or_create_by_date(date)

        grid_response = get_board_response(sudoku, user)

        return JsonResponse({
            'id': sudoku.pk,
            'date': datetime.date.strftime(date, "%d-%m-%Y"),
            'board': grid_response
        }, safe=False)

class Save(APIView):
    def post(self, request: HttpRequest) -> JsonResponse:
        body = json.loads(request.body)
        sudoku_pk = body[KEY_ID]
        board = body[KEY_BOARD]
        user = get_ip_address_user_from_request(request)
        sudoku = Sudoku.objects.get(pk=sudoku_pk)

        [user_sudoku, _] = UserSudoku.objects.get_or_create(user=user, sudoku=sudoku)
        user_sudoku.progress = board
        user_sudoku.save()

        return JsonResponse({'success': True})

class Check(APIView):
    def post(self, request: HttpRequest) -> JsonResponse:
        body = json.loads(request.body)
        sudoku_pk = body[KEY_ID]
        board = body[KEY_BOARD]

        sudoku = Sudoku.objects.get(pk=sudoku_pk)
        solution = sudoku.solution

        errors = []
        for row_i, row in enumerate(board):
            for col_i, cell in enumerate(row):
                if (not cell.value):
                    continue
                if (cell.value == solution[row_i][col_i]):
                    continue
                errors.append({
                    'rowIndex': row_i,
                    'colIndex': col_i
                })

        return JsonResponse(errors)

def map_row_to_response_board(row):
    return list(map(lambda cell: {
        'value': cell,
        'isFixed': cell > 0,
        'possibleValues': []
    }, row))

def get_board_response(sudoku: Sudoku, user: IPAddressUser):
    if (UserSudoku.objects.filter(user=user.pk, sudoku=sudoku.pk).exists()):
            user_sudoku = UserSudoku.objects.get(user=user.pk, sudoku=sudoku.pk)
            if (user_sudoku.progress):
                return user_sudoku.progress

    starting_board = sudoku.start

    return list(map(map_row_to_response_board, starting_board))
