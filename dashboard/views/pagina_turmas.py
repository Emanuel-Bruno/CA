from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .tipo_usuario import tipo_usuario

@login_required
def pagina_turmas_aluno(request, usuario):
    context = {
        'usuario': usuario
    }

    return render(
        request,
        'dashboard/turmas.html',
        context
    )

@login_required
def pagina_turmas_professor(request, usuario):
    context = {
        'usuario': usuario
    }

    return render(
        request,
        'dashboard/turmas.html',
        context
    )

@login_required
def pagina_turmas_administrador(request):
    return redirect(reverse_lazy('admin:index'))

@login_required
def pagina_turmas(request):
    usuario = tipo_usuario(request.user)
    if usuario:
        if usuario['tipo'] == 'aluno':
            return pagina_turmas_aluno(
                request, 
                usuario
            )

        if usuario['tipo']== 'professor':
            return pagina_turmas_professor(
                request, 
                usuario
            )

        if usuario['tipo']== 'administrador':
            return pagina_turmas_administrador(request)
            
    return render(
        request, 
        'person403.html', 
        {
            'message': 'Usuário sem vinculo'
        }
    )