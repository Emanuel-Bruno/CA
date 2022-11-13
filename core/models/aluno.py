from django.db import models
from django.contrib.auth.models import User
from datetime import date
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

    @property
    def turmas_atuais(self):
        turmas = []
        data = date.today()
        for registro in self.registro_set.all():

            if registro.turma and registro.turma.periodo and data > registro.turma.periodo.data_inicio and data < registro.turma.periodo.data_final:      
                turmas.append(registro.turma)

        return turmas

    @property
    def get_qtd_turmas_atuais(self):
        turmas = []
        data = date.today()
        for registro in self.registro_set.all():

            if registro.turma and registro.turma.periodo and data > registro.turma.periodo.data_inicio and data < registro.turma.periodo.data_final:      
                turmas.append(registro.turma)

        return len(turmas)



    def __str__(self):
        return self.nome

    class Meta:
        app_label = 'core'
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
