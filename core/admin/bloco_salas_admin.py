from django.contrib import admin

from ..models import BlocoSalas


@admin.register(BlocoSalas)
class BlocoSalasAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nome',
    ]

    search_fields = [
        'id',
        'nome',
    ]
