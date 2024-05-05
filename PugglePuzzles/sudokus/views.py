from rest_framework.views import APIView
from django.http import HttpRequest, JsonResponse
from sudokus.models import Sudoku, UserSudoku
from main.models import IPAddressUser
from main.utils import get_ip_address_user_from_request

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

        try:
            sudoku = Sudoku.objects.get(pk=pk)
        except Sudoku.DoesNotExist:
            return JsonResponse({"error": "Sudoku could not be found"}, status=404)

        return JsonResponse({"id": sudoku.pk, "start": sudoku.start})
