from django.db import models
from usuarios.models import Usuario


# Create your models here.

# Clase que renderiza las categorias:

class Categoria(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    activo = models.BooleanField(default=True)
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']

#Clase que renderiza las publicaciones

class Publicaciones(models.Model):
    fecha = models.DateField(auto_now_add=True)
    titulo = models.CharField(max_length=255)
    post = models.TextField()
    update = models.DateTimeField(auto_now=True)
    categoria = models.ForeignKey(Categoria, on_delete= models.SET_NULL, related_name='posteos', null=True)
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='posteos_usuario')
    
    def __str__(self):
        return self.titulo
 
    




