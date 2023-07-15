from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Usuario
from .forms import RegistrarseForm

# Create your views here.

class RegistroView(CreateView):
    model = Usuario
    template_name = 'usuarios/registro.html'
    form_class = RegistrarseForm
