from django.contrib import admin

from ..models import Disciplina


class DisciplinaInline(admin.StackedInline):
    model = Disciplina

    extra = 0
