from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from aplicaciones.usuarios.views import CrearUsuario

urlpatterns = [
    # path('inicio_usuario/',InicioUsuario.as_view(),name = 'inicio_usuarios'),
    # path('listado_usuarios/',ListarUsuario.as_view(),{'parametro_extra':'Hola!'},name = 'listar_usuarios'),
    # path('registrarse',CrearUsuario.as_view(),name = 'registrar_usuario'),
    #USUARIOS
    # path('login',views.IniciarSesion.as_view(),name='login'),
    # path('registrarse',views.RegistrarUsuario.as_view(),name='registra_usuario')
]