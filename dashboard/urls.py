from django.urls import path
from .views import pagina_inicial
from .views import pagina_notas
from .views import pagina_turma
from .views import pagina_turma_frequencia
from .views import pagina_turma_notas
from .views import pagina_turma_tarefas
from .views import pagina_turmas
urlpatterns = [
    path('', pagina_inicial, name='pagina_inicial'),
    path('notas/', pagina_notas, name='pagina_notas'),
    path('turmas-frequencia/<int:id>/', pagina_turma_frequencia, name='pagina_turma_frequencia'),
    path('turmas-notas/<int:id>/', pagina_turma_notas, name='pagina_turma_notas'),
    path('turmas-tarefas/<int:id>/', pagina_turma_tarefas, name='pagina_turma_tarefas'),
    path('turmas-noticias/<int:id>/', pagina_turma, name='pagina_turma'),
    path('turmas-tarefaform/<int:id>/', pagina_turma_tarefaform, name='pagina_turma_tarefaform'),
    path('turmas-noticiaform/<int:id>/', pagina_turma_noticiaform, name='pagina_turma_noticiaform'),
    path('turmas/', pagina_turmas, name='pagina_turmas'),
]
