from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
from distutils.command.upload import upload


# Create your models here.

class TipoTaller(models.Model):
    id_tipo = models.IntegerField(null=False, primary_key=True)
    tipo = models.CharField(max_length=20)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.tipo
    class Meta:
        db_table = 'db_tipo_taller'


class Taller(models.Model):
    codigo = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=300)
    tipo = models.ForeignKey(TipoTaller, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="talleres", null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'db_taller'

class Postulacion(models.Model):
    codigo = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to="postulaciones", null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'db_postulacion'

class Reporte(models.Model):
    codigo = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to="reportes", null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'db_reporte'

class Materiales(models.Model):
    codigo = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to="materiales", null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'db_materiales'




class Usuario(models.Model):
    run = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    region= models.CharField(max_length=50)
    direccion= models.CharField(max_length=80)
    correo = models.CharField(max_length=120)
    telefono = models.IntegerField()
    imagen = models.ImageField(upload_to="usuariosadulmayor", null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'db_usuario'





class Usuarioinstructor(models.Model):
    run = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    region= models.CharField(max_length=50)
    direccion= models.CharField(max_length=80)
    correo = models.CharField(max_length=120)
    telefono = models.IntegerField()
    imagen = models.ImageField(upload_to="usuariosinstructor", null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'db_usuario_instructor'


class Usuariofuncionario(models.Model):
    run = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    region= models.CharField(max_length=50)
    direccion= models.CharField(max_length=80)
    correo = models.CharField(max_length=120)
    telefono = models.IntegerField()
    imagen = models.ImageField(upload_to="usuariosfuncionario", null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'db_usuario_funcionario'

class Usuarioadmin(models.Model):
    run = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    region= models.CharField(max_length=50)
    direccion= models.CharField(max_length=80)
    correo = models.CharField(max_length=120)
    telefono = models.IntegerField()
    imagen = models.ImageField(upload_to="usuariosadmin", null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'db_usuario_administrador'





class CarroTaller(models.Model):
    taller = models.ForeignKey(Taller, on_delete=models.CASCADE)

    class Meta:
        db_table = 'db_carrotaller'



class ItemsTaller(models.Model):
    codigoTaller = models.IntegerField()
    nombreTaller = models.CharField(max_length=40)
    descripcionTaller=models.CharField(max_length=300)
    imagen = models.ImageField(upload_to="items_taller", null=True)

    def __str__(self):
        return self.nombreTaller
    
    class Meta:
        db_table = 'db_items_taller'


