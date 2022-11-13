from django import template
register = template.Library()
from core.models import Aluno, Professor, Administrador

@register.simple_tag
def tipo_usuario(usuario):

    try:
        Aluno.objects.get(usuario=usuario)
        return 'aluno'

    except:
        pass

    try:
        Professor.objects.get(usuario=usuario)
        return 'professor'

    except:
        pass

    try:
        Administrador.objects.get(usuario=usuario)
        return 'administrador'
        
    except:
        pass

    return None