from django.db import models


class Curso(models.Model):
    '''
    A classe Curso serve para armazernar os(as) cursos do sistema.
    Além de fazer as implementações relacionadas a um único objeto do tipo Curso.
    '''

    nome = models.CharField(
        verbose_name='Nome',
        max_length=100
    )

    def __str__(self):
        return self.nome

    class Meta:
        app_label = 'core'
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
