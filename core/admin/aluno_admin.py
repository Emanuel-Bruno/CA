from django.contrib import admin

from ..models import Aluno
from .registro_inline import RegistroInline

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nome',
        'usuario',
        'vinculos',
        'turmas_atuais'
    ]

    search_fields = [
        'id',
        'nome',
        'usuario'
    ]

    inlines = [RegistroInline]