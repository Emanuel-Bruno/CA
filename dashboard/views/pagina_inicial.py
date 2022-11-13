from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .tipo_usuario import tipo_usuario
from django.http import HttpResponseNotFound, Http404

@login_required
def pagina_inicial_aluno(request, usuario):
    context = {
        'usuario': usuario
    }

    return render(
        request,
        'dashboard/inicial.html',
        context
    )

@login_required
def pagina_inicial_professor(request, usuario):
    context = {
        'usuario': usuario
    }

    return render(
        request,
        'dashboard/inicial.html',
        context
    )

@login_required
def pagina_inicial_administrador(request):
    return redirect(reverse_lazy('admin:index'))

@login_required
def pagina_inicial(request):
    usuario = tipo_usuario(request.user)
    if usuario:
        if usuario['tipo'] == 'aluno':
            return pagina_inicial_aluno(
                request, 
                usuario
            )

        if usuario['tipo']== 'professor':
            return pagina_inicial_professor(
                request, 
                usuario
            )

        if usuario['tipo']== 'administrador':
            return pagina_inicial_administrador(request)
            
    return render(
        request, 
        'person403.html', 
        {
            'message': 'Usuário sem vinculo'
        }
    )
    
