from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Professor(models.Model):
    '''
    A classe Professor serve para armazernar os(as) professores do sistema.
    Além de fazer as implementações relacionadas a um único objeto do tipo Professor.
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
    def turmas_atuais(self):
        from .turma import Turma
        turmas = []
        data = date.today()
        for turma in Turma.objects.filter(professor=self):
            if turma.periodo and data > turma.periodo.data_inicio and data < turma.periodo.data_final:      
                turmas.append(turma)

        return turmas

    @property
    def get_qtd_turmas_atuais(self):

        return len(self.turmas_atuais)

    def __str__(self):
        return self.nome

    class Meta:
        app_label = 'core'
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'
