from django.db import models
from django.contrib.auth.models import User

class Aluno(models.Model):
    '''
    A classe Aluno serve para armazernar os(as) aluno do sistema.
    Além de fazer as implementações relacionadas a um único objeto do tipo Aluno.
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

    @property
    def vinculos(self):
        vinculos = ''
        for vinculo in self.vinculo_set.all():
            vinculos = f'{vinculo} '
        return vinculos

    def __str__(self):
        return self.nome

    class Meta:
        app_label = 'core'
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
