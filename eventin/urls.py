from django.urls import path
from .views import participantes

urlpatterns = [
    path("", participantes),
]