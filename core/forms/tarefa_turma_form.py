from django import forms

from ..models import TarefaTurma


class TarefaTurmaForm(forms.ModelForm):
    class Meta:
        model = TarefaTurma

        fields = ['turma', 'titulo', 'descricao', 'anexo']
