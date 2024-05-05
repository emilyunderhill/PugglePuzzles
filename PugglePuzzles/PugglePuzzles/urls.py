from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from sudokus import urls as sudoku_urls

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/sudokus/', include(sudoku_urls)),
]
