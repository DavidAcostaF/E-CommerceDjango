from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView,View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout

from . import models
from . import forms
from . import mixins
# Create your views here.

class Login(FormView):
    template_name = 'login.html'
    form_class = forms.FormularioLogin
    success_url = reverse_lazy('index')
    
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,**kwargs)

    def form_valid(self,form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)


def logoutUsuario(request):
    logout(request)
    return redirect('index') 

class CrearUsuario(CreateView):
    model = models.Usuario
    form_class = forms.FormularioUsuario
    template_name = 'registrar.html'
    success_url = reverse_lazy('login')

    def post(self,request,*args,**kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                print(form.cleaned_data.get('email'))
                print(form.cleaned_data.get('username'))
                nuevo_usuario = models.Usuario(
                    email = form.cleaned_data.get('email'),
                    username = form.cleaned_data.get('username'),
                    nombres = form.cleaned_data.get('nombres'),
                    apellidos = form.cleaned_data.get('apellidos')
                )
                nuevo_usuario.set_password(form.cleaned_data.get('password1'))
                print(nuevo_usuario)
                nuevo_usuario.save()
                mensaje = f'{self.model.__name__} registrado correctamente'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
                #return redirect('usuarios:listar_usuarios')
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
                #return render(request,self.template_name,{'form':form})
        else:
            return redirect('login')
