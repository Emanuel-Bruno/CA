from django.contrib import admin

from ..models import Professor


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
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
