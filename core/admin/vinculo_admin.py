from django.contrib import admin

from ..models import Vinculo


@admin.register(Vinculo)
class VinculoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        '__str__'
    ]

    search_fields = [
        'id',
        '__str__'
    ]

    filter_horizontal = [
        'alunos'
    ]