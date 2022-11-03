from django.contrib import admin

from ..models import Turma


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nome',
        'periodo',
        'curso'
    ]

    search_fields = [
        'id',
        'nome',
        'periodo',
        'curso'
    ]

    list_filter = [
        'periodo',
        'curso'
    ]
