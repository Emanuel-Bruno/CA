from django.contrib import admin

from ..models import Registro


class RegistroInline(admin.StackedInline):
    model = Registro

    extra = 0
