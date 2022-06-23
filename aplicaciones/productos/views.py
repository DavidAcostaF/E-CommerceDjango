from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView,View

from . import models
from . import forms
from aplicaciones.usuarios.models import Usuario
# Create your views here.
#principal
class Inicio(TemplateView):
    template_name = 'index.html'

class CrearProductos(CreateView):
    model = models.CrearProducto
    form_class = forms.FormularioProducto
    template_name = 'productos/crear_productos.html'
    success_url = reverse_lazy('productos:crear_productos')


class ListarProductos(ListView):
    model = models.CrearProducto
    template_name = 'productos/lista_productos.html'
    context_object_name = 'productos'

    def get_queryset(self):
        return self.model.objects.filter(estado = True)    


    #HACER ESTO r.article_set.count()
    # 2
    # def get(self,request):
    #     print(serializers.serialize('json',self.get_queryset()),'application/json')
    #     if request.headers.get('x-requested-with') == 'XMLHttpRequest': # Se encuentra en la documentación de Django 4.0
    #         print(serializers.serialize('json',self.get_queryset()),'application/json')
    #         return HttpResponse(serializers.serialize('json',self.get_queryset()),'application/json')
    #     else:
    #         return redirect('/')

class EliminarProductos(DeleteView):
    model = models.CrearProducto
    template_name = 'productos/eliminar_producto.html'
    success_url = reverse_lazy('index')

    # def get(self,request,pk):
    #     return print(self.model.objects.filter(id = pk))

    def post(self,request,pk,*args, **kwargs):
        producto = self.model.objects.get(id = pk)
        producto.estado = False
        producto.save()
        return redirect(self.success_url)

class EditarProducto(UpdateView):
    model = models.CrearProducto
    template_name = 'productos/editar_producto.html'
    form_class = forms.FormularioProducto
    success_url = reverse_lazy('index')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['producto'] = self.model.objects.filter(estado = True)
        return context

    # def get_success_url(self):
    #     return redirect(self.success_url)


#CARRITO

class Carrito(CreateView):
    model = models.Carrito
    form_class = forms.FormularioCarrito
    template_name = 'carrito/agregar_carrito.html'
    success_url = reverse_lazy('index')
#Agregar producto al carrito
    def post(self, request):
        user_id = request.POST.get('user')
        producto_id = request.POST.get('producto')
        user = Usuario.objects.get(id=user_id)
        print(user_id,producto_id)
        producto = models.CrearProducto.objects.get(id=producto_id)
        carrito, created = models.Carrito.objects.get_or_create(usuario=user, producto=producto)
        if not created:
            carrito.cantidad += 1
            carrito.save()

        print(carrito)
        return HttpResponse(status=200)

        # vista = Vista(
        #     algo='algo'
        # )

class VerCarrito(ListView):
    model = models.Carrito
    template_name = 'carrito/ver_carrito.html'
    context_object_name = 'carrito'

    def get_queryset(self,user_id):
        return self.model.objects.filter(usuario = user_id)

    def get(self,request):
            return render(request,self.template_name,{'context':self.get_queryset(request.user.id)})

        # if request.headers.get('x-requested-with') == 'XMLHttpRequest': # Se encuentra en la documentación de Django 4.0
        #     return render(request,self.template_name,{'context':self.get_queryset(request.user.id)})
        #     return HttpResponse(serializers.serialize('json',self.get_queryset(request.user.id)),'application/json')

    def post(self,request):
        producto = request.POST.get('producto')
        cantidad = request.POST.get('cantidad')
        producto = models.CrearProducto.objects.get(id = producto)
        models.DetalleVenta.objects.create(producto = producto,cantidad = cantidad)
        return render(request,self.template_name,{'context':self.get_queryset(request.user.id)})
        
        # models.CrearProducto.objects.create()


class ListarCarrito(View):
    def get(self,request):
        carrito = models.Carrito.objects.filter(usuario = request.user)
        user = Usuario.objects.get(id=request.user.id)
        venta = models.Venta.objects.create(usuario = user)
        for item in carrito:
            models.DetalleVenta.objects.create(venta = venta,producto=item.producto,cantidad=item.cantidad)
        carrito.delete()
        return redirect('/')
    """
    un boton que al darle click consulte todo lo del carrito, despues crea instancia de la venta y las instancias DellateVenta y despues borra lo del carrito
    http://127.0.0.1:8000/listar_carrito/
    """
    
