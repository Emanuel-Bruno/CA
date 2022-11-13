from django.contrib import admin

from ..models import Registro


@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'turma',
        'aluno',
    ]

    search_fields = [
        'id',
        'turma',
        'aluno'
    ]

    list_filter = [
        'aluno',
        'turma'
    ]

    autocomplete_fields = [
        'aluno',
        'turma'
    ]
