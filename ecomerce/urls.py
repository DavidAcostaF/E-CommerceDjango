"""ecomerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import static
from django.conf import settings
from aplicaciones.productos.views import Inicio
from django.contrib.auth.decorators import login_required
from aplicaciones.usuarios.views import Login,CrearUsuario,logoutUsuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Inicio.as_view(),name = 'index'),
    path('',include(('aplicaciones.productos.urls','productos'))),
    path('',include(('aplicaciones.usuarios.urls','usuarios'))),
    path('accounts/login/',Login.as_view(),name = 'login'),
    path('accounts/register',CrearUsuario.as_view(),name = 'register'),
    path('logout/',login_required(logoutUsuario),name = 'logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
