from django.db import models
from .periodo import Periodo
from .aluno import Aluno
from .curso import Curso

class Vinculo(models.Model):
    '''
    A classe Vinculo serve para armazernar os(as) vinculos do sistema.
    Além de fazer as implementações relacionadas a um único objeto do tipo Vinculo.
    '''

    periodo_inicio = models.ForeignKey(
        Periodo,
        verbose_name='Período',
        on_delete=models.SET_NULL,
        null=True
    )

    curso = models.ForeignKey(
        Curso,
        verbose_name='Curso',
        on_delete=models.SET_NULL,
        null=True
    )

    alunos = models.ManyToManyField(
        Aluno,
        verbose_name='Alunos',
        null=True
    )
    
    def __str__(self):
        return f'{self.id} - {self.periodo_inicio} | {self.curso}'

    class Meta:
        app_label = 'core'
        verbose_name = 'Vinculo'
        verbose_name_plural = 'Vinculos'
