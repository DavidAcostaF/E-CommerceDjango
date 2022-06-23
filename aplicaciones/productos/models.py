from django.db import models
from aplicaciones.usuarios.models import Usuario
# Create your models here.

class CrearProducto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre del Producto',max_length=100,blank=False,null=False)
    descripcion = models.TextField('Descripcion',max_length=200,blank=False,null=False)
    costo = models.CharField('Costo',max_length=50,blank=False,null=False)
    imagen = models.ImageField('Imagen',upload_to ='media')
    estado = models.BooleanField('Estado',default=True)
    fecha_registro = models.DateField('Fecha de registro',auto_now=True,auto_now_add=False)

    class Meta:
        verbose_name = 'CrearProducto'
        verbose_name_plural = 'CrearProductos'
        ordering = ['nombre']
        
    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    id = models.AutoField(primary_key=True)
    producto = models.ForeignKey(CrearProducto,on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    
    
class Venta(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    fecha_venta = models.DateField(auto_now=False,auto_now_add=True)
    # total = models.FloatField()
    
class DetalleVenta(models.Model):
    producto = models.ForeignKey(CrearProducto,on_delete=models.CASCADE)
    venta = models.ForeignKey(Venta,on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def precio_producto(self):
        return self.producto.costo*self.cantidad