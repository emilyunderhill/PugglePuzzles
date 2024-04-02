import datetime
from rest_framework.views import APIView
from django.http import HttpRequest, JsonResponse
from sudokus.models import Sudoku

KEY_DATE = 'date'
KEY_ID = 'id'
KEY_START = 'start'

class Sudokus(APIView):
    def get(self, request: HttpRequest) -> JsonResponse:
        date = request.GET.get(KEY_DATE)

        try:
            date_obj = datetime.strptime(date, '%Y-%m-%d').date()
        except (TypeError, ValueError):
            return JsonResponse({"error": "Invalid date format. Please provide date in YYYY-MM-DD format."}, status=400)

        try:
            sudoku = Sudoku.objects.get(created_at=date_obj)
        except Sudoku.DoesNotExist:
            return JsonResponse({"error": "No Sudoku puzzle created on the specified date"}, status=404)

        start = sudoku.start
        id = sudoku.pk
        return JsonResponse({ id, start })

class Solution(APIView):
    def get(self, request: HttpRequest) -> JsonResponse:
        id = request.GET.get(KEY_ID)

        try:
            sudoku = Sudoku.objects.get(pk=id)
        except Sudoku.DoesNotExist:
            return JsonResponse({"error": "Sudoku puzzle could not be found"}, status=404)

        solution = sudoku.solution
        return JsonResponse({ id, solution })
