from rest_framework.views import APIView
from django.http import HttpRequest, JsonResponse
from sudokus.models import Sudoku, UserSudoku
from main.models import IPAddressUser
from main.utils import get_ip_address_user_from_request
import json, datetime
from datetime import date

KEY_ID = 'id'
KEY_DATE = 'date'

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
        pk = request.GET.get(KEY_ID)

        user = get_ip_address_user_from_request(request)

        date_str = request.GET.get(KEY_DATE)
        if (not date_str):
            date = datetime.date.today()
        else:
            date = datetime.datetime.strptime(date_str, "%d-%m-%Y")

        sudoku: Sudoku = Sudoku.objects.find_or_create_by_date(date)

        starting_board = json.loads(sudoku.start)

        grid_response = list(map(map_row_to_response_board, starting_board))

        if (UserSudoku.objects.filter(user=user.pk, sudoku=sudoku.pk).exists()):
            user_sudoku = UserSudoku.objects.get(user=user.pk, sudoku=sudoku.pk)
            for i_r, row in enumerate(user_sudoku):
                for i_c, cell in enumerate(row):
                    grid_response[i_r][i_c]['value'] = cell

        return JsonResponse({
            'id': sudoku.pk,
            'date': datetime.date.strftime(date, "%d-%m-%Y"),
            'board': grid_response
        }, safe=False)

def map_row_to_response_board(row):
    return list(map(lambda cell: {
        'value': cell,
        'isFixed': cell > 0,
        'possibleValues': []
    }, row))
