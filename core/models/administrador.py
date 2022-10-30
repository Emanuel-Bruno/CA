from django.db import models
from django.contrib.auth.models import User


class Administrador(models.Model):
    '''
    A classe Administrador serve para armazernar os(as) Administradores do sistema.
    Além de fazer as implementações relacionadas a um único objeto do tipo Administrador.
    '''

    nome = models.CharField(
        verbose_name='Nome',
        max_length=100
    )

    usuario = models.ForeignKey(
        User,
        verbose_name='Usuário',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.nome

    class Meta:
        app_label = 'core'
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'
