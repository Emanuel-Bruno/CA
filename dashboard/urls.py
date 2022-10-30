from django.urls import path
from .views import pagina_inicial
urlpatterns = [
    path('inicial/', pagina_inicial, name='pagina_inicial'),
]
