from rest_framework.views import APIView
from django.http import HttpRequest, JsonResponse
from sudokus.models import Sudoku

KEY_ID = 'id'

class List(APIView):
    def get(self, request: HttpRequest) -> JsonResponse:
        sudokus = Sudoku.objects.order_by('-id').values_list('id', flat=True)[:5]

        return JsonResponse({'ids': list(sudokus)})

class Start(APIView):
    def get(self, request: HttpRequest) -> JsonResponse:
        pk = request.GET.get(KEY_ID)

        try:
            sudoku = Sudoku.objects.get(pk=pk)
        except Sudoku.DoesNotExist:
            return JsonResponse({"error": "Sudoku could not be found"}, status=404)

        return JsonResponse({"id": sudoku.pk, "start": sudoku.start})
