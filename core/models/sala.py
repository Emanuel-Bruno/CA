from django.db import models
from .bloco_salas import BlocoSalas

class Sala(models.Model):
    '''
    A classe Sala serve para armazernar os(as) salas do sistema.
    Além de fazer as implementações relacionadas a um único objeto do tipo Sala.
    '''

    bloco_salas = models.ForeignKey(
        BlocoSalas,
        verbose_name='Bloco de Salas',
        on_delete=models.SET_NULL,
        null=True
    )

    numero = models.IntegerField(
        verbose_name='Número',
        null=True
    )

    def __str__(self):
        str_return = f''

        if self.bloco_salas and self.numero:
            str_return += f'{self.bloco_salas} - '
            
        str_return += f'{self.numero}'

        return str_return

    class Meta:
        app_label = 'core'
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'
