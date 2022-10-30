from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def pagina_inicial(request):
    context = {
        
    }

    return render(
        request,
        'dashboard/inicial.html',
        context
    )
