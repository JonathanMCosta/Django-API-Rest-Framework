from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from eventin.views import (
    EventoViewSet, ParticipanteViewSet, InscricaoViewSet,
    ListaInscricoesEventos, ListaIncricoesParticipantes)

router = routers.DefaultRouter()
router.register("eventos", EventoViewSet, basename="Eventos")
router.register("participantes", ParticipanteViewSet, basename="Participantes")
router.register("inscricoes", InscricaoViewSet, basename="Inscrições")

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
    path('participantes/<int:pk>/inscricoes', ListaIncricoesParticipantes.as_view()),
    path('eventos/<int:pk>/inscricoes', ListaInscricoesEventos.as_view()),
]
