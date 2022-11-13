from django import forms

from ..models import NoticiaTurma


class NoticiaTurmaForm(forms.ModelForm):
    class Meta:
        model = NoticiaTurma

        fields = '__all__'
