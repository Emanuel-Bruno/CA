from django.contrib import admin

from ..models import Aluno


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nome',
        'usuario'
    ]

    search_fields = [
        'id',
        'nome',
        'usuario'
    ]
