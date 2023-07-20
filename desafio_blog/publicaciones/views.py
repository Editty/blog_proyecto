from django.shortcuts import render
from .models import Publicaciones, Comentario
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from publicaciones.forms import CrearPublicacionForm, ComentarioForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins import SuperUsuarioAutorMixin

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
    
    def form_valid(self, form):
        f = form.save(commit=False) # Esta linea de código pausa la ejecución del form y no lo guarda
        f.creador_del_posteo_id = self.request.user.id
        return super().form_valid(f)
    
# View que actualiza/edita una publicacion ya existente

class EditarPost(SuperUsuarioAutorMixin, LoginRequiredMixin, UpdateView):
    model = Publicaciones  
    template_name = 'publicaciones/editar-post.html' 
    form_class = CrearPublicacionForm 
    
    def get_success_url(self):
        return reverse('publicaciones:publicaciones')
    
# View que elimina un posteo ya existente:

class EliminarPost(SuperUsuarioAutorMixin, LoginRequiredMixin, DeleteView):
    model = Publicaciones
    template_name = 'publicaciones/eliminar-post.html'
    
    def get_success_url(self):
        return reverse('publicaciones:publicaciones')
      

# Views que se encarga de mostrar un objeto en detalle:

class PostDetalle(DetailView):
    model = Publicaciones
    template_name = 'publicaciones/detalle-post.html'
    context_object_name = 'detalle'
    
    # Se redefine el metodo get_context_data() para que se muestre el formulario en la misma ventana
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['formulario_comentario'] = ComentarioForm()
        return contexto
    
    # Se redefine el metodo post() para que guarde los comentarios en una tabla de la base de datos
    def post(self, request , *args, **kwargs):
        publicaciones = self.get_object() # ESTA VARIABLE VA A ALMACENAR EL OBJETO DEL DETALLE COMPLETO
        formulario = ComentarioForm(request.POST) # ESTA VARIABLE RECUPERA LA DATA QUE TIENE EL FORMULARIO Y LA GUARDA EN UNA TABLA
        
        if formulario.is_valid():
            comentario = formulario.save(commit=False)
            comentario.autor_id = self.request.user.id
            comentario.relacion_post = publicaciones
            comentario.save()
            return super().get(request)
        else:
            return super().get(request)
       

# View que borra comentarios
class BorrarComentarioView(DeleteView):
    model = Comentario
    template_name = 'publicaciones/borrar-comentario.html'
    
    def get_success_url(self):
        return reverse('publicaciones:detalle-posteo', args = [self.object.relacion_post.id])
    
