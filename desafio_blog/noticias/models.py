from django.db import models
from usuarios.models import Usuario

# Create your models here.

class Noticias(models.Model):
    fecha = models.DateField(auto_now_add=True)
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    autor_noticia = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='autor_noticias')

    def __str__(self):
        return self.titulo