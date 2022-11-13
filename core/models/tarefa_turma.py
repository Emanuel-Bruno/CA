from django.db import models
from .turma import Turma
from crum import get_current_user

class TarefaTurma(models.Model):
    '''
    A classe TarefaTurma serve para armazernar os(as) tarefas do sistema.
    Além de fazer as implementações relacionadas a um único objeto do tipo TarefaTurma.
    '''

    turma = models.ForeignKey(
        Turma,
        verbose_name='Turma',
        on_delete=models.SET_NULL,
        null=True
    )

    titulo = models.CharField(
        verbose_name='Titulo',
        max_length=100
    )

    descricao = models.TextField(
        verbose_name="Descrição"
    )

    anexo = models.FileField(
        verbose_name='Anexo',
        upload_to='anexos/files/',
        null=True,
        blank=True
    )

    data_criacao = models.DateTimeField(
        verbose_name='Data de Criação',
        auto_now_add=True,
        null=True
    )

    data_atualizacao = models.DateTimeField(
        verbose_name='Data de Atualização',
        auto_now=True,
        null=True
    )
    
    usuario_criacao = models.ForeignKey(
		'auth.User', 
        verbose_name='Usuário de Criação',
		related_name='%(class)s_requests_created',
		blank=True, null=True,
        on_delete=models.SET_NULL,
	)

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):

        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_criacao = user
        
        super(TarefaTurma, self).save(*args, **kwargs)

    class Meta:
        app_label = 'core'
        verbose_name = 'Tarefa da Turma'
        verbose_name_plural = 'Tarefas da Turma'
