from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Noticias
from django.views.generic import ListView, CreateView
from django.urls import reverse
from .forms import CrearNoticiasForm

# Create your views here.

class VerNoticias(ListView):
    model = Noticias
    template_name = 'noticias/noticias.html'
    context_object_name = 'noticias'

    def get_queryset(self):
        consulta_anterior = super().get_queryset()
        consulta_ordenada = consulta_anterior.order_by('fecha')
        return consulta_ordenada
    
class CrearNoticia(CreateView):
    model = Noticias
    template_name = 'noticias/crear-noticia.html'
    form_class = CrearNoticiasForm

    def get_success_url(self):
        return reverse('noticias:noticias')
    
    def form_valid(self, form):
        f = form.save(commit=False) 
        f.autor_noticia_id = self.request.user.id
        return super().form_valid(f)