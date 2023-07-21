from django import forms
from .models import Noticias


class CrearNoticiasForm(forms.ModelForm):
    class Meta:
        model = Noticias
        fields = [ 'titulo', 'texto']