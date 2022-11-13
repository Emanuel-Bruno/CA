from django.db import models


class BlocoSalas(models.Model):
    '''
    A classe Bloco serve para armazernar os(as) bloco de salas do sistema.
    Além de fazer as implementações relacionadas a um único objeto do tipo Bloco.
    '''

    nome = models.CharField(
        verbose_name='Nome',
        max_length=100
    )

    def __str__(self):
        return self.nome

    class Meta:
        app_label = 'core'
        verbose_name = 'Bloco de Salas'
        verbose_name_plural = 'Blocos de Salas'
