from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

name = "productos"
urlpatterns = [
    path('crear_productos/',login_required(views.CrearProductos.as_view()),name = 'crear_productos'),
    path('lista_productos/',views.ListarProductos.as_view(),name = 'listar_productos'),
    path('eliminar_producto/<int:pk>/',login_required(views.EliminarProductos.as_view()),name = 'eliminar_productos'),
    path('editar_producto/<int:pk>',login_required(views.EditarProducto.as_view()),name = 'editar_productos'),
    #CARRITO
    path('agregar_carrito/',login_required(views.Carrito.as_view()),name = 'agregar_carrito'),
    path('carrito/',login_required(views.VerCarrito.as_view()),name = 'carrito'),
    path('comprar_productos/',login_required(views.ComprarCarrito.as_view()),name = 'comprar_productos'),
    path('historial_compras/',login_required(views.HistorialCompras.as_view()),name = 'historial_compras'),
    path('cantidad/',login_required(views.Cantidad.as_view()),name = 'cantidad')
]