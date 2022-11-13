from core.models import Aluno, Professor, Administrador

def tipo_usuario(usuario):
    try:
        return {
            'usuario': Aluno.objects.get(usuario=usuario), 
            'tipo': 'aluno'
        }

    except:
        pass

    try:
        return {
            'usuario': Professor.objects.get(usuario=usuario), 
            'tipo': 'professor'
        }

    except:
        pass

    try:
        return {
            'usuario': Administrador.objects.get(usuario=usuario), 
            'tipo': 'administrador'
        }
        
    except:
        pass
    
    return None