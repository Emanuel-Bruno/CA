from django.contrib import admin

from ..models import NoticiaTurma


class NoticiaTurmaInline(admin.StackedInline):
    model = NoticiaTurma

    extra = 0
