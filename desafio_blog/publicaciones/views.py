from django.shortcuts import render
from .models import Publicaciones
from django.views.generic import ListView, CreateView, UpdateView
from publicaciones.forms import CrearPublicacionForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

#View basada en clases que renderiza las publicaciones

class VerPublicaciones(ListView):
    model = Publicaciones
    template_name = 'publicaciones/publicaciones.html'
    context_object_name = 'posteos'
    
    def get_queryset(self):
        publicaciones = super().get_queryset()
        return publicaciones.order_by('fecha')
    
# View que crea posteos    
    
class Postear(LoginRequiredMixin, CreateView):
    model = Publicaciones
    template_name = 'publicaciones/postear.html'
    form_class = CrearPublicacionForm
    
    def get_success_url(self):
        return reverse('publicaciones:publicaciones')
    
# View que actualiza/edita una publicacion ya existente

class EditarPost(LoginRequiredMixin, UpdateView):
    model = Publicaciones  #Nombre de la clase del archivo models.py
    template_name = 'publicaciones/editar-post.html' #Nombre de la carpeta/nombre del template archivo.html
    form_class = CrearPublicacionForm #Nombre de la clase que esta en el archivo forms.py
    
    def get_success_url(self):
        return reverse('publicaciones:publicaciones')
    
    
    

