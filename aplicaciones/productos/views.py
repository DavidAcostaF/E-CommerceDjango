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


class EliminarProductos(DeleteView):
    model = models.CrearProducto
    template_name = 'productos/eliminar_producto.html'
    success_url = reverse_lazy('index')


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
        producto = models.CrearProducto.objects.get(id=producto_id)
        carrito, created = models.Carrito.objects.get_or_create(usuario=user, producto=producto)
        if not created:
            carrito.cantidad += 1
            carrito.save()
        return HttpResponse(status=200)

        # vista = Vista(
        #     algo='algo'
        # )

class VerCarrito(View):
    model = models.Carrito
    template_name = 'carrito/ver_carrito.html'
    context_object_name = 'carrito'

    def get_queryset(self,user_id):
        return self.model.objects.filter(usuario = user_id)

    def get(self,request):
            return render(request,self.template_name,{'context':self.get_queryset(request.user.id)})
    
    def post(self,request):
        print(request.POST.get('id'))
        producto = request.POST.get('producto')
        cantidad = request.POST.get('cantidad')
        if producto and cantidad:
            producto = models.CrearProducto.objects.get(id = producto)
            models.DetalleVenta.objects.create(producto = producto,cantidad = cantidad)
            return render(request,self.template_name,{'context':self.get_queryset(request.user.id)})
        else:
            cantidades = request.POST.get('cantidades')
            productos = request.POST.get('productos')
            carrito = models.Carrito.objects.get(id = productos)
            carrito.cantidad = cantidades
            carrito.save()



class ComprarCarrito(View):
    def get(self,request):
        carrito = models.Carrito.objects.filter(usuario = request.user)
        user = Usuario.objects.get(id=request.user.id)
        venta = models.Venta.objects.create(usuario = user)
        for item in carrito:
            models.DetalleVenta.objects.create(venta = venta,producto=item.producto,cantidad=item.cantidad)
        carrito.delete()
        return redirect('index')

    

class HistorialCompras(View):
    model = models.DetalleVenta
    template_view = 'productos/historial_compras.html'

    def get(self,request):
        detalleventa = models.DetalleVenta.objects.filter(venta__usuario=request.user)
        return render(request,'productos/historial_compras.html',{'detalleventa':detalleventa})

class Cantidad(DeleteView):

    def post(self,request):
        req = request.POST.get('id')
        print(req)
        borrar = models.Carrito.objects.filter(id = req)
        borrar.delete()
        return redirect('carrito')