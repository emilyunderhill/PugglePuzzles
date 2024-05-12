from django.urls import path
from .views import List, Start, Save, Check

urlpatterns = [
    path('all', List.as_view()),
    path('get', Start.as_view()),
    path('save', Save.as_view()),
    path('check', Check.as_view()),
]
