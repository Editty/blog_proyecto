from django import forms
from .models import Publicaciones


class CrearPublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicaciones
        fields = ['categoria', 'titulo', 'post']
        
        widgets = {
            # AGREGAMOS LA CLAVE/VALOR DE 'CATEGORIA' EN EL DICCIONARIO WIDGETS
            'categoria': forms.Select(attrs={'class': 'form-select', 'placeholder':'Categoria'}),
            'titulo': forms.TextInput(attrs={'placeholder': 'Aca va el titulo', 'class': 'from-control'}),
            'post': forms.Textarea(attrs={'placeholder': 'Dejanos un Comentario aqui...', 'class': 'from-control'}),
        }

