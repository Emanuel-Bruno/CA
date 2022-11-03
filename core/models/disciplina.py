from django.db import models
from .curso import Curso

class Disciplina(models.Model):
    '''
    A classe Disciplina serve para armazernar os(as) disciplinas do sistema.
    Além de fazer as implementações relacionadas a um único objeto do tipo Disciplina.
    '''

    nome = models.CharField(
        verbose_name='Nome',
        max_length=100
    )

    curso = models.ForeignKey(
        Curso,
        verbose_name='Curso',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.nome

    class Meta:
        app_label = 'core'
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'
