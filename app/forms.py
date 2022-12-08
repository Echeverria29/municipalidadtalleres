from genericpath import exists
from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model= User 
        fields = ['username','password1','password2']

class TallerForm(ModelForm):

    codigo = forms.IntegerField(min_value=1)
    nombre = forms.CharField(min_length=3 ,max_length=20)
    descripcion = forms.CharField(min_length=3 ,max_length=300)




    class Meta:
        
        model = Taller
      
        fields = ['codigo','nombre', 'descripcion','tipo', 'imagen']

class PostulacionForm(ModelForm):

    codigo = forms.IntegerField(min_value=1)
    nombre = forms.CharField(min_length=3 ,max_length=20)
    descripcion = forms.CharField(min_length=3 ,max_length=300)




    class Meta:
        
        model = Postulacion
      
        fields = ['codigo','nombre', 'descripcion', 'imagen']

class Reporte(ModelForm):

    codigo = forms.IntegerField(min_value=1)
    nombre = forms.CharField(min_length=3 ,max_length=20)
    descripcion = forms.CharField(min_length=3 ,max_length=300)




    class Meta:
        
        model = Reporte
      
        fields = ['codigo','nombre', 'descripcion', 'imagen']

class MaterialesForm(ModelForm):

    codigo = forms.IntegerField(min_value=1)
    nombre = forms.CharField(min_length=3 ,max_length=20)
    descripcion = forms.CharField(min_length=3 ,max_length=300)




    class Meta:
        
        model = Materiales
      
        fields = ['codigo','nombre', 'descripcion', 'imagen']

   
          
        


class UsuarioForm(ModelForm):
    run = forms.IntegerField(min_value=1)
    nombre = forms.CharField(min_length=3 ,max_length=20)
    apellido= forms.CharField(min_length=2 ,max_length=20)
    comuna = forms.CharField(min_length=3 ,max_length=20)
    region = forms.CharField(min_length=3 ,max_length=20)
    direccion = forms.CharField(min_length=2 ,max_length=20)
    correo = forms.CharField(min_length=3 ,max_length=20)
    telefono = forms.IntegerField(min_value=1)

    class Meta:
        model = Usuario
        fields = ['run','nombre','apellido','comuna','region','direccion','correo','telefono', 'imagen']

class UsuarioForminstructor(ModelForm):
    run = forms.IntegerField(min_value=1)
    nombre = forms.CharField(min_length=3 ,max_length=20)
    apellido= forms.CharField(min_length=2 ,max_length=20)
    comuna = forms.CharField(min_length=3 ,max_length=20)
    region = forms.CharField(min_length=3 ,max_length=20)
    direccion = forms.CharField(min_length=2 ,max_length=20)
    correo = forms.CharField(min_length=3 ,max_length=20)
    telefono = forms.IntegerField(min_value=1)

    class Meta:
        model = Usuarioinstructor
        fields = ['run','nombre','apellido','comuna','region','direccion','correo','telefono', 'imagen']

class UsuarioFormfuncionario(ModelForm):
    run = forms.IntegerField(min_value=1)
    nombre = forms.CharField(min_length=3 ,max_length=20)
    apellido= forms.CharField(min_length=2 ,max_length=20)
    comuna = forms.CharField(min_length=3 ,max_length=20)
    region = forms.CharField(min_length=3 ,max_length=20)
    direccion = forms.CharField(min_length=2 ,max_length=20)
    correo = forms.CharField(min_length=3 ,max_length=20)
    telefono = forms.IntegerField(min_value=1)

    class Meta:
        model = Usuariofuncionario
        fields = ['run','nombre','apellido','comuna','region','direccion','correo','telefono', 'imagen']

class UsuarioFormadmin(ModelForm):
    run = forms.IntegerField(min_value=1)
    nombre = forms.CharField(min_length=3 ,max_length=20)
    apellido= forms.CharField(min_length=2 ,max_length=20)
    comuna = forms.CharField(min_length=3 ,max_length=20)
    region = forms.CharField(min_length=3 ,max_length=20)
    direccion = forms.CharField(min_length=2 ,max_length=20)
    correo = forms.CharField(min_length=3 ,max_length=20)
    telefono = forms.IntegerField(min_value=1)

    class Meta:
        model = Usuarioadmin
        fields = ['run','nombre','apellido','comuna','region','direccion','correo','telefono', 'imagen']



class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']

