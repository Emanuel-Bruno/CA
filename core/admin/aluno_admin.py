from django.contrib import admin

from ..models import Aluno
from .registro_inline import RegistroInline
from import_export.admin import ImportExportModelAdmin

@admin.register(Aluno)
class AlunoAdmin(ImportExportModelAdmin):
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