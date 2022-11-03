from django.contrib import admin

from ..models import Administrador


@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
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
