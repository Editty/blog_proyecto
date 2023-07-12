from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Publicaciones
from django.views.generic import ListView

# Create your views here.

class VerPublicaciones(ListView):
    model = Publicaciones
    template_name = 'publicaciones/publicaciones.html'
    context_object_name = 'publicaciones'
    
    def get_queryset(self):
        publicaciones = super().get_queryset()
        return publicaciones.order_by('fecha')
    
