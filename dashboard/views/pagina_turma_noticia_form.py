from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .tipo_usuario import tipo_usuario
from core.forms import NoticiaTurmaForm
from core.models import Turma

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
    turma = Turma.objects.get(id=id)
    form=NoticiaTurmaForm(initial={'turma': turma})
    if request.method == 'POST':
        form = NoticiaTurmaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(f'/turmas-noticias/{id}/')
    context = {
        'usuario': usuario,
        'form': form,
        'turma': turma
    }

    return render(
        request,
        'dashboard/turma_noticias_form.html',
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