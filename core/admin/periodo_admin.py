from django.contrib import admin

from ..models import Periodo


@admin.register(Periodo)
class PeriodoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        '__str__',
    ]

    search_fields = [
        'id',
        '__str__',
    ]
