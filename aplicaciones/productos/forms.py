from django import forms
from django.contrib.auth.models import User
from . import models

class FormularioProducto(forms.ModelForm):
    class Meta:
        model = models.CrearProducto
        fields = ['nombre','descripcion','costo','imagen']
        labels = {
            'nombre ':'Nombre del producto',
            'descripcion ':'Descripcion del Producto',
            'costo ':'Costo del Producto',
            'imagen ':'Imagen del Producto'     
        }
        
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Nombre del Producto',
                }),
            'descripcion':forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Descripcion del producto'
                }),
            'costo': forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Precio del Producto'
                }),
            'imagen': forms.FileInput(
                attrs = {
                    'class':'form-control',
            })
        }


class FormularioCarrito(forms.ModelForm):
    class Meta:
        model = models.Carrito
        fields = ['producto','usuario']
        labels ={
            'producto':'ID del producto',
            'usuario':'ID del usuario'}
        widgets = {
            'producto': forms.NumberInput(
                attrs ={
                    'id':'producto'
                } 
            ),
            'usuario':forms.NumberInput(
                attrs ={
                    'id':'producto'
                }
            )
        }



            
