from django.urls import path
from .views import List, Start

urlpatterns = [
    path('all', List.as_view()),
    path('get', Start.as_view()),
]
