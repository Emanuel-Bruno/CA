from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .tipo_usuario import tipo_usuario
from core.models import Registro, Turma, TarefaTurma

@login_required
def pagina_turma_tarefas_aluno(request, usuario, id):
    try:
        turma = Turma.objects.get(id=id)
        aluno = usuario['usuario']
        if not Registro.objects.filter(aluno=aluno, turma=turma).exists():
            return render(
                request, 
                'person403.html', 
                {
                    'message': 'Você não tem acesso a essa turma'
                }
            )
    except:
        return render(
            request, 
            'person404.html', 
            {
                'message': 'Turma não encontrada'
            }
        )
    context = {
        'turma': turma,
        'usuario': usuario,
        'tarefas': TarefaTurma.objects.filter(turma=turma)
    }

    return render(
        request,
        'dashboard/turma_tarefas.html',
        context
    )

@login_required
def pagina_turma_tarefas_professor(request, usuario, id):
    context = {
        'usuario': usuario
    }

    return render(
        request,
        'dashboard/turma_tarefas.html',
        context
    )

@login_required
def pagina_turma_tarefas_administrador(request):
    return redirect(reverse_lazy('admin:index'))

@login_required
def pagina_turma_tarefas(request, id):
    usuario = tipo_usuario(request.user)
    if usuario:
        if usuario['tipo'] == 'aluno':
            return pagina_turma_tarefas_aluno(
                request, 
                usuario,
                id
            )

        if usuario['tipo']== 'professor':
            return pagina_turma_tarefas_professor(
                request, 
                usuario,
                id
            )

        if usuario['tipo']== 'administrador':
            return pagina_turma_tarefas_administrador(request)
            
    return render(
        request, 
        'person403.html', 
        {
            'message': 'Usuário sem vinculo'
        }
    )
    
