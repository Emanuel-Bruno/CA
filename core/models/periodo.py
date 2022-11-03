from django.db import models


class Periodo(models.Model):
    '''
    A classe Periodo serve para armazernar os(as) periodos do sistema.
    Além de fazer as implementações relacionadas a um único objeto do tipo Periodo.
    '''

    data_inicio = models.DateField(
        verbose_name='Data Inicial',
        null=True
    )

    data_final = models.DateField(
        verbose_name='Data Final',
        null=True
    )

    def __str__(self):
        return_str = f''
        if self.data_inicio:
            return_str += f'{self.data_inicio} | '

        if self.data_final:
            return_str += f'{self.data_final}'
        
        return return_str

    class Meta:
        app_label = 'core'
        verbose_name = 'Período'
        verbose_name_plural = 'Períodos'
