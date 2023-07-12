from django.shortcuts import render
from .models import Publicaciones
from django.views.generic import ListView, CreateView
from publicaciones.forms import CrearPublicacionForm
from django.urls import reverse

# Create your views here.

class VerPublicaciones(ListView):
    model = Publicaciones
    template_name = 'publicaciones/publicaciones.html'
    context_object_name = 'posteos'
    
    def get_queryset(self):
        publicaciones = super().get_queryset()
        return publicaciones.order_by('fecha')
    
class Postear(CreateView):
    model = Publicaciones
    template_name = 'publicaciones/postear.html'
    form_class = CrearPublicacionForm
    
    def get_success_url(self):
        return reverse('publicaciones:publicaciones')

