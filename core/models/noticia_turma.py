from django.db import models
from .turma import Turma
from crum import get_current_user

class NoticiaTurma(models.Model):
    '''
    A classe NoticiaTurma serve para armazernar os(as) Notícias da Turma do sistema.
    Além de fazer as implementações relacionadas a um único objeto do tipo NoticiaTurma.
    '''

    turma = models.ForeignKey(
        Turma,
        verbose_name='Turma',
        on_delete=models.SET_NULL,
        null=True
    )

    titulo = models.CharField(
        verbose_name='Título',
        max_length=100
    )

    texto = models.TextField(
        verbose_name='Texto',
        max_length=500
    )

    data_criacao = models.DateTimeField(
        verbose_name='Data de Criação',
        auto_now_add=True
    )

    data_atualizacao = models.DateTimeField(
        verbose_name='Data de Atualização',
        auto_now=True
    )
    
    usuario_criacao = models.ForeignKey(
		'auth.User', 
        verbose_name='Usuário de Criação',
		related_name='%(class)s_requests_created',
		blank=True, null=True,
        on_delete=models.SET_NULL,
	)

    def save(self, *args, **kwargs):

        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_criacao = user
        
        super(NoticiaTurma, self).save(*args, **kwargs)


    def __str__(self):
        return self.titulo

    class Meta:
        app_label = 'core'
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'
        ordering = ['data_atualizacao', '-id']
