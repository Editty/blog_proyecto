from django.db import models
from django.views.generic import ListView


# Create your models here.

class Publicaciones(models.Model):
    fecha = models.DateField(auto_now_add=True)
    titulo = models.CharField(max_length=255)
    post = models.TextField()
    
    def __str__(self):
        return self.titulo
    
# Clase que renderiza las categorias
class Categoria(models.Model,ListView):
    nombre = models.CharField(max_length=200, unique=True)
    activo = models.BooleanField(default=True)
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        consulta = super().__str__()
        return consulta.order_by('nombre')
    




