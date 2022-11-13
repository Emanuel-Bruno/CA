from django.contrib import admin

from ..models import TarefaTurma


@admin.register(TarefaTurma)
class TarefaTurmaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'turma',
        'titulo',
    ]

    search_fields = [
        'id',
        'turma',
        'titulo'
    ]

    list_filter = [
        'turma'
    ]

    autocomplete_fields = [
        'turma'
    ]
