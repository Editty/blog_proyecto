from django.db import models

# Create your models here.

class Publicaciones(models.Model):
    fecha = models.DateField(auto_now_add=True)
    titulo = models.CharField(max_length=255)
    post = models.TextField()
    
    def __str__(self):
        return self.titulo
