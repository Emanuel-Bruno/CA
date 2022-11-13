from django.db import models

from .disciplina import Disciplina
from .periodo import Periodo
from .curso import Curso
from .professor import Professor
from .sala import Sala

class Turma(models.Model):
    '''
    A classe Turma serve para armazernar os(as) turmas do sistema.
    Além de fazer as implementações relacionadas a um único objeto do tipo Turma.
    '''
    
    nome = models.CharField(
        verbose_name='Nome',
        max_length=100
    )
    periodo = models.ForeignKey(
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

    disciplinas_equivalente = models.ManyToManyField(
        Disciplina,
        verbose_name='Disciplinas Equivalentes',
        null=True
    )

    STATUS_CHOICES = (
        ('Cadastrando', 'Cadastrando'),
        ('Cadastro Finalizado','Cadastro Finalizado'),
        ('Andamento','Andamento'),
        ('Concluído','Concluído'),
        ('Cancelada', 'Cancelada')
    )

    status = models.CharField(
        verbose_name='Status',
        max_length=100,
        choices=STATUS_CHOICES,
        default=('Cadastrando', 'Cadastrando')
    )

    sala = models.ForeignKey(
        Sala,
        verbose_name='Sala',
        on_delete=models.SET_NULL,
        null=True,
    )

    professor = models.ForeignKey(
        Professor,
        verbose_name='Professor',
        on_delete=models.SET_NULL,
        null=True,
    )

    horario = models.CharField(
        verbose_name='horario',
        max_length=100,
        default='',
        blank=True
    )


    def __str__(self):
        return self.nome

    class Meta:
        app_label = 'core'
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
