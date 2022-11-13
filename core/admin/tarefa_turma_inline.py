from django.contrib import admin

from ..models import TarefaTurma


class TarefaTurmaInline(admin.StackedInline):
    model = TarefaTurma
    extra = 0
