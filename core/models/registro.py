from django.db import models
from .aluno import Aluno
from .turma import Turma

class Registro(models.Model):
    '''
    A classe Registro serve para armazernar os(as) registros do sistema.
    Além de fazer as implementações relacionadas a um único objeto do tipo Registro.
    '''

    aluno = models.ForeignKey(
        Aluno,
        verbose_name='Aluno',
        on_delete=models.SET_NULL,
        null=True
    )

    turma = models.ForeignKey(
        Turma,
        verbose_name='Turma',
        on_delete=models.SET_NULL,
        null=True
        
    )

    nota1 = models.DecimalField(
        verbose_name='Nota 1ª Unidade',
        default=0,
        decimal_places=2,
        max_digits=5
    )

    nota2 = models.DecimalField(
        verbose_name='Nota 2ª Unidade',
        default=0,
        decimal_places=2,
        max_digits=5
    )

    nota3 = models.DecimalField(
        verbose_name='Nota 3ª Unidade',
        default=0,
        decimal_places=2,
        max_digits=5
    )

    nota_recuperacao = models.DecimalField(
        verbose_name='Nota da Recuperacao',
        default=0,
        decimal_places=2,
        max_digits=5
    )
    SITUACAO_CHOICES = (
        ('Reprovado', 'Reprovado'),
        ('Aprovado', 'Aprovado'),
        ('Em andamento', 'Em andamento'),
    )

    situacao = models.CharField(
        verbose_name='Situação',
        max_length=100,
        choices=SITUACAO_CHOICES,
        default='Em andamento',
    )

    @property
    def media(self):
        media = (self.nota1 + self.nota2 + self.nota3)/3
        
        if media >= 7:
            return media

        if media >=3:
            media = (self.nota1 + self.nota2 + self.nota3 + self.nota_recuperacao)/4

        return media

    def __str__(self):
        return f'{self.aluno} - {self.turma}'

    class Meta:
        app_label = 'core'
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'
