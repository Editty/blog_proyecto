from django.contrib.auth.mixins import UserPassesTestMixin

class SuperUsuarioAutorMixin(UserPassesTestMixin):
    def test_func(self):
        usuario = self.request.user
        publicacion = self.get_object()
        
        return usuario == publicacion.creador_del_posteo or usuario.is_superuser