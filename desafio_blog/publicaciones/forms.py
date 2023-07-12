from django.forms import ModelForm
from .models import Publicaciones


class CrearPublicacionForm(ModelForm):
    class Meta:
        model = Publicaciones
        fields = ['titulo', 'post']
