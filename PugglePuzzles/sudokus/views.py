from rest_framework.views import APIView
from django.http import HttpRequest, JsonResponse
from sudokus.models import Sudoku, UserSudoku
from main.models import IPAddressUser
from main.utils import get_ip_address_user_from_request
import json

KEY_ID = 'id'

class List(APIView):
    def get(self, request: HttpRequest) -> JsonResponse:
        user = get_ip_address_user_from_request(request)

        sudokus = Sudoku.objects.order_by('-id')[:10]

        response = []
        for sudoku in sudokus:
            if (not UserSudoku.objects.filter(user=user.pk, sudoku=sudoku.pk).exists()):
                response.append({
                    'id': sudoku.pk,
                    'solved': False,
                    'inProgress': False
                })
            else:
                user_sudoku = UserSudoku.objects.get(user=user.pk, sudoku=sudoku.pk)
                response.append({
                    'id': sudoku.pk,
                    'solved': user_sudoku.completed,
                    'inProgress': not user_sudoku.completed
                })


        return JsonResponse(response, safe=False)

class Start(APIView):
    def get(self, request: HttpRequest) -> JsonResponse:
        pk = request.GET.get(KEY_ID)

        user = get_ip_address_user_from_request(request)

        try:
            sudoku = Sudoku.objects.get(pk=pk)
        except Sudoku.DoesNotExist:
            return JsonResponse({"error": "Sudoku could not be found"}, status=404)

        starting_board = json.loads(sudoku.start)

        grid_response = list(map(map_row_to_response_board, starting_board))

        if (UserSudoku.objects.filter(user=user.pk, sudoku=sudoku.pk).exists()):
            user_sudoku = UserSudoku.objects.get(user=user.pk, sudoku=sudoku.pk)
            for i_r, row in enumerate(user_sudoku):
                for i_c, cell in enumerate(row):
                    grid_response[i_r][i_c]['value'] = cell

        return JsonResponse({
            'id': sudoku.pk,
            'board': grid_response
        }, safe=False)

def map_row_to_response_board(row):
    return list(map(lambda cell: {
        'value': cell,
        'isFixed': cell > 0,
        'possibleValues': []
    }, row))
