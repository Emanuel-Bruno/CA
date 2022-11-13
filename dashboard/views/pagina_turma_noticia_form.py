from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .tipo_usuario import tipo_usuario
from core.forms import NoticiaTurmaForm

@login_required
def pagina_turma_noticia_form_aluno(request, usuario, id):
    return render(
        request, 
        'person403.html', 
        {
            'message': 'Você não tem acesso a essa página'
        }
    )

@login_required
def pagina_turma_noticia_form_professor(request, usuario, id):
    form=NoticiaTurmaForm(initial={'turma':id})
    context = {
        'usuario': usuario,
        'form': form
    }

    return render(
        request,
        'dashboard/turmas.html',
        context
    )

@login_required
def pagina_turma_noticia_form_administrador(request):
    return redirect(reverse_lazy('admin:index'))

@login_required
def pagina_turma_noticia_form(request, id):
    usuario = tipo_usuario(request.user)
    if usuario:
        if usuario['tipo'] == 'aluno':
            return pagina_turma_noticia_form_aluno(
                request, 
                usuario,
                id
            )

        if usuario['tipo']== 'professor':
            return pagina_turma_noticia_form_professor(
                request, 
                usuario,
                id
            )

        if usuario['tipo']== 'administrador':
            return pagina_turma_noticia_form_administrador(request)
            
    return render(
        request, 
        'person403.html', 
        {
            'message': 'Usuário sem vinculo'
        }
    )