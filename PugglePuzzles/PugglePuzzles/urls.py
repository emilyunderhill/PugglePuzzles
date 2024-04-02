from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from sudokus.views import Sudokus

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/sudokus', Sudokus.as_view()),
]
