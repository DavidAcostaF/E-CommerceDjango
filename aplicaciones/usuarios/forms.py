from django import forms
from django.contrib.auth.forms import AuthenticationForm

from . import models

class FormularioLogin(AuthenticationForm):
    def __init__(self,*args, **kwargs):
        super(FormularioLogin,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

class FormularioUsuario(forms.ModelForm):
    """Formulario de registro de un usuario de la base de datos

        Varibles:

        - password1 : Contraseña
        - password2: Verificacion de la contraseña
    """
    password1 = forms.CharField(label = 'Contraseña',widget=forms.PasswordInput(
        attrs = {
            'class':'form-control',
            'placeholder':'Ingrese su contraseña...',
            'id':'password1',
            'required':'required'
        })
    )

    password2 = forms.CharField(label='Contraseña de confirmacion',widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese nuevamente su contraseña...',
            'id':'password2',
            'required':'required'
        }
    ))

    class Meta:
        model = models.Usuario
        fields = ('username','email','nombres','apellidos',)
        labels = {
            'username':'Nombre de usuario',
            'email':'Correo del usuario',
            'nombres':'Nombres',
            'apellidos':'Apellidos'
        }
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre de usuario',
                }),
            'email': forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Correo Electronico',
                }),
            'nombres': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su nombres',
                }),
            'apellidos': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese sus apellidos',
                }
            ),
        }
    def clean_password2(self):
        """Validacion de Contraseña

        Metodo que valida que ambas contraseñas ingresadas sean iguales esto antes de ser encriptadas y guardadas en la base de datos, Retornar la contraseña valida

        Excepciones:
        -ValidationError Cuando las contraseñas no son iguales muestra mensaje de error
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden')
        return password2

    def save(self,commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user