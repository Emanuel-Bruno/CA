from django.contrib import admin

from ..models import Curso
from .disciplina_inline import DisciplinaInline

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nome'
    ]

    search_fields = [
        'id',
        'nome'
    ]

    inlines = [DisciplinaInline]