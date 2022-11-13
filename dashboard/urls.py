from django.urls import path
from .views import pagina_inicial
from .views import pagina_notas
from .views import pagina_turma
from .views import pagina_turmas
urlpatterns = [
    path('', pagina_inicial, name='pagina_inicial'),
    path('notas/', pagina_notas, name='pagina_notas'),
    path('turmas/<int:id>/', pagina_turma, name='pagina_turma'),
    path('turmas/', pagina_turmas, name='pagina_turmas'),
]
