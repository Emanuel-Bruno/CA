from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .tipo_usuario import tipo_usuario
from core.models import Registro, Turma
from decimal import Decimal
@login_required
def pagina_turma_notas_aluno(request, usuario, id):
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
        'registros': Registro.objects.filter(aluno=aluno, turma=turma)
    }

    return render(
        request,
        'dashboard/turma_notas.html',
        context
    )

@login_required
def pagina_turma_notas_professor(request, usuario, id):

    try:
        turma = Turma.objects.get(id=id, professor=usuario['usuario'])
        if not Registro.objects.filter(turma=turma).exists():
            return render(
                request, 
                'person403.html', 
                {
                    'message': 'Você não tem acesso a essa turma'
                }
            )
        
        if request.method == 'POST':
            registro = request.POST.get('registro')
            nota1 = Decimal(request.POST.get('nota1'))
            nota2 = Decimal(request.POST.get('nota2'))
            nota3 = Decimal(request.POST.get('nota3'))
            nota_recuperacao = request.POST.get('nota_recuperacao', None)
            nota_recuperacao = None if nota_recuperacao == '' else nota_recuperacao
            nota_recuperacao = Decimal(nota_recuperacao) if nota_recuperacao else None
            situacao = request.POST.get('situacao')

            registro = Registro.objects.get(id=registro)
            registro.nota1 = nota1
            registro.nota2 = nota2
            registro.nota3 = nota3
            registro.nota_recuperacao = nota_recuperacao
            registro.situacao = situacao
            registro.save()
            return redirect(f'/turmas-notas/{id}/')

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
        'registros': turma.registro_set.all()[:10],
        'options_situacao': Registro.SITUACAO_CHOICES
    }
    return render(
        request,
        'dashboard/turma_notas.html',
        context
    )

@login_required
def pagina_turma_notas_administrador(request):
    return redirect(reverse_lazy('admin:index'))

@login_required
def pagina_turma_notas(request, id):
    usuario = tipo_usuario(request.user)
    if usuario:
        if usuario['tipo'] == 'aluno':
            return pagina_turma_notas_aluno(
                request, 
                usuario,
                id
            )

        if usuario['tipo']== 'professor':
            return pagina_turma_notas_professor(
                request, 
                usuario,
                id
            )

        if usuario['tipo']== 'administrador':
            return pagina_turma_notas_administrador(request)
            
    return render(
        request, 
        'person403.html', 
        {
            'message': 'Usuário sem vinculo'
        }
    )
    
