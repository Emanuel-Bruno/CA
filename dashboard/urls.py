from django.urls import path
from .views import pagina_inicial
from .views import pagina_notas
from .views import pagina_turma
from .views import pagina_turma_frequencia
from .views import pagina_turma_notas
from .views import pagina_turma_tarefas
from .views import pagina_turmas
from .views import pagina_turma_tarefa_form
from .views import pagina_turma_noticia_form
urlpatterns = [
    path('', pagina_inicial, name='pagina_inicial'),
    path('notas/', pagina_notas, name='pagina_notas'),
    path('turmas-frequencia/<int:id>/', pagina_turma_frequencia, name='pagina_turma_frequencia'),
    path('turmas-notas/<int:id>/', pagina_turma_notas, name='pagina_turma_notas'),
    path('turmas-tarefas/<int:id>/', pagina_turma_tarefas, name='pagina_turma_tarefas'),
    path('turmas-noticias/<int:id>/', pagina_turma, name='pagina_turma'),
    path('turmas-tarefa-form/<int:id>/', pagina_turma_tarefa_form, name='pagina_turma_tarefa_form'),
    path('turmas-noticia-form/<int:id>/', pagina_turma_noticia_form, name='pagina_turma_noticia_form'),
    path('turmas/', pagina_turmas, name='pagina_turmas'),
]
