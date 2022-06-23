from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.CrearProducto)
admin.site.register(models.Carrito)
admin.site.register(models.Venta)
admin.site.register(models.DetalleVenta)
