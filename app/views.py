from urllib import request
from django.http import response
from django.shortcuts import render,redirect

# Create your views here.

import requests
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, permission_required


def index(request):
  return render(request,'app/index.html')

def nosotros(request):
    return render(request,'app/nosotros.html')

def perfil(request):
    return render(request,'app/perfil.html')

@login_required
def caliestrellas(request):
  return render(request,'app/caliestrellas.html')

@login_required
def pagos(request):
  return render(request,'app/pagos.html')


#REPORTE
@login_required
def reporte(request):
    datos = {
        'form' : Reporte()
    }
    if request.method == 'POST' :
        formulario = Reporte (request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Reporte enviado correctamente!')


    return render(request,'app/reporte.html', datos)

#POSTULACION
@login_required
def postulacionform(request):
    datos = {
        'form' : PostulacionForm
    }
    if request.method == 'POST' :
        formulario = Postulacion (request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Postulacion enviada correctamente!')


    return render(request,'app/postulacionform.html', datos)

@login_required
def modifipostulacion (request, codigo):
    taller = Postulacion.objects.get(codigo=codigo)
    datos = {
        'form' : PostulacionForm(instance=taller)
    }
    if request.method == 'POST':
        formulario = PostulacionForm(data=request.POST, files=request.FILES, instance=taller)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, '¡Modificación exitosa!')
            datos['form'] = formulario

    return render(request, 'app/modifipostulacion.html', datos)

#ELIMINAR FUNCIONNARIO
def eliminarpostulacion(request,codigo):

  fun = Postulacion.objects.get(codigo=codigo)
  fun.delete()
  messages.success(request,'Postulacion eliminada!')

  return redirect(to="listaperfilfuncionario")
#TERMINA AQUI





#MATERIALES
@login_required
def materialesform(request):
    datos = {
        'form' : MaterialesForm()
    }
    if request.method == 'POST' :
        formulario = MaterialesForm (request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Materiales enviada correctamente!')


    return render(request,'app/materialesform.html', datos)


@login_required
def modifimate (request, codigo):
    taller = Materiales.objects.get(codigo=codigo)
    datos = {
        'form' : MaterialesForm(instance=taller)
    }
    if request.method == 'POST':
        formulario = MaterialesForm(data=request.POST, files=request.FILES, instance=taller)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, '¡Modificación exitosa!')
            datos['form'] = formulario

    return render(request,'app/modifimate.html', datos)


#ELIMINAR FUNCIONNARIO
def eliminarmate(request,codigo):

  fun = Materiales.objects.get(codigo=codigo)
  fun.delete()
  messages.success(request,'Materiales eliminados!')

  return redirect(to=listarmateriales)
#TERMINA AQUI



#CRUD ADULTO MAYOR
#FORMULARIO PARA GUARDAR EL ADULTO MAYOR
@login_required
def usuarioform(request):
    datos = {
        'form' : UsuarioForm()
    }
    if request.method == 'POST' :
        formulario = UsuarioForm (request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Datos del usuario guradados correctamente!')


    return render(request,'app/usuarioform.html', datos)

#FORMULARIO PARA MODIFICAR DATOS ADULTO MAYOR 
@login_required
def modifiadultomayor (request, run):
    usuario = Usuario.objects.get(run=run)
    datos = {
        'form' : UsuarioForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, files=request.FILES, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, '¡Modificación exitosa!')
            datos['form'] = formulario

    return render(request, 'app/modifiadultomayor.html', datos)

#ELIMINAR ADULTO MAYOR
def eliminaradultomayor(request,run):

  adultom = Usuario.objects.get(run=run)
  adultom.delete()
  messages.success(request,'Adulto mayor eliminado eliminado!')

  return redirect(to="listaperfil")
#TERMINA AQUI






#CRUD INSTRUCTOR
#FORMULARIO PARA AGREGAR DATOS INSTRUCTOR
def usuarioforminstructor(request):
    datos = {
        'form' : UsuarioForminstructor()
    }
    if request.method == 'POST' :
        formulario = UsuarioForminstructor (request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Datos del instructor guradados correctamente!')


    return render(request,'app/usuarioforminstructor.html', datos)

#MODIFICIAR INSTRUCTOR
@login_required
def modifinstructor (request, run):
    usuario = Usuarioinstructor.objects.get(run=run)
    datos = {
        'form' : UsuarioForminstructor(instance=usuario)
    }
    if request.method == 'POST':
        formulario = UsuarioForminstructor(data=request.POST, files=request.FILES, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, '¡Modificación exitosa!')
            datos['form'] = formulario

    return render(request, 'app/modifinstructor.html', datos)

#ELIMINAR INSTRUCTOR
def eliminarinstructor(request,run):

  instru = Usuarioinstructor.objects.get(run=run)
  instru.delete()
  messages.success(request,'Instructor eliminado!')

  return redirect(to="listaperfilinstructor")
#TERMINA AQUI





#CRUD FUNCIONARIO
#FORMULARIO PARA AGREGAR UN FUNCIONARIO
def usuarioformfuncionario(request):
    datos = {
        'form' : UsuarioFormfuncionario()
    }
    if request.method == 'POST' :
        formulario = UsuarioFormfuncionario (request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Datos del funcionario guradados correctamente!')


    return render(request,'app/usuarioformfuncionario.html', datos)

#MODIFICAR EL FUNCIONARIO 
@login_required
def modififuncionario (request, run):
    usuario = Usuariofuncionario.objects.get(run=run)
    datos = {
        'form' : UsuarioFormfuncionario(instance=usuario)
    }
    if request.method == 'POST':
        formulario = UsuarioFormfuncionario(data=request.POST, files=request.FILES, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, '¡Modificación exitosa!')
            datos['form'] = formulario

    return render(request, 'app/modififuncionario.html', datos)


#ELIMINAR FUNCIONNARIO
def eliminarfuncionario(request,run):

  funcio = Usuariofuncionario.objects.get(run=run)
  funcio.delete()
  messages.success(request,'Funcionario eliminado!')

  return redirect(to="listaperfilfuncionario")
#TERMINA AQUI





#CRUD ADMIN
def usuarioformadmin(request):
    datos = {
        'form' : UsuarioFormadmin()
    }
    if request.method == 'POST' :
        formulario = UsuarioFormadmin (request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Datos del administrador guradados correctamente!')


    return render(request,'app/usuarioformadmin.html', datos)

#MODIFICAR EL ADMIN
@login_required
def modifiadmin (request, run):
    usuario = Usuarioadmin.objects.get(run=run)
    datos = {
        'form' : UsuarioFormadmin(instance=usuario)
    }
    if request.method == 'POST':
        formulario = UsuarioFormadmin(data=request.POST, files=request.FILES, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, '¡Modificación exitosa!')
            datos['form'] = formulario

    return render(request, 'app/modifiadmin.html', datos)


#ELIMINAR FUNCIONNARIO
def eliminaradmin(request,run):

  admin = Usuarioadmin.objects.get(run=run)
  admin.delete()
  messages.success(request,'administrador eliminado!')

  return redirect(to="listaperfiladmin")
#TERMINA AQUI




#CREAR FUNCIONARIO DE ADMIN
def usuarioformfunadmin(request):
    datos = {
        'form' : UsuarioFormadmin()
    }
    if request.method == 'POST' :
        formulario = UsuarioFormadmin (request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Datos del funcionario guardados correctamente!')


    return render(request,'app/usuarioformfunadmin.html', datos)

@login_required
def modififunadmin (request, run):
    usuario = Usuariofuncionario.objects.get(run=run)
    datos = {
        'form' : UsuarioFormfuncionario(instance=usuario)
    }
    if request.method == 'POST':
        formulario = UsuarioFormfuncionario(data=request.POST, files=request.FILES, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, '¡Modificación exitosa!')
            datos['form'] = formulario

    return render(request, 'app/modififunadmin.html', datos)


#ELIMINAR FUNCIONNARIO
def eliminarfunadmin(request,run):

  admin = Usuariofuncionario.objects.get(run=run)
  admin.delete()
  messages.success(request,'administrador eliminado!')

  return redirect(to="listaperfiladmin")
#TERMINA AQUI





#CREAR ADULTO MARYOR DE ADMIN
def usuarioformaduladmin(request):
    datos = {
        'form' : UsuarioForm()
    }
    if request.method == 'POST' :
        formulario = UsuarioForm (request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Datos del adulto mayor guardados correctamente!')


    return render(request,'app/usuarioformaduladmin.html', datos)



#CREAR INSTRUCTOR DE ADMIN
def usuarioforminstadmin(request):
    datos = {
        'form' : UsuarioForminstructor()
    }
    if request.method == 'POST' :
        formulario = UsuarioForminstructor (request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Datos del instructor guardados correctamente!')


    return render(request,'app/usuarioforminstadmin.html', datos)







#FORMULARIO PARA GUARDAR EL TALLER EL FUNCIONARIO
@login_required
def agregartaller(request):
    datos = {
        'form' : TallerForm()
    }
    if request.method == 'POST' :
        formulario = TallerForm (request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Taller guardado!')


    return render(request,'app/agregartaller.html', datos)



#FORMULARIO PARA GUARDAR EL TALLER EL ADMIN
@login_required
def agregartalleradmin(request):
    datos = {
        'form' : TallerForm()
    }
    if request.method == 'POST' :
        formulario = TallerForm (request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Taller guardado!')


    return render(request,'app/agregartalleradmin.html', datos)

#ELIMINAR EL TALLER GUARDADO
def eliminartaller(request,codigo):

  tallers = Taller.objects.get(codigo=codigo)
  tallers.delete()
  messages.success(request,'Taller eliminado!')

  return redirect(to="talleresfuncionario")

#LISTAR LOS DATOS PARA CADA PERFIL POR SEPARADO
# LISTAR DATOS DE ADULTO MAYOR
@login_required
def listaperfil(request):
    
    usuarioall = Usuario.objects.all()
    datos = {
      'listaPerfil' : usuarioall
    }
    return render(request,'app/listaperfil.html',datos)

#LISTAR DATOS PARA EL INSTRUCTOR
def listaperfilinstructor(request):
    
    usuarioall2 = Usuarioinstructor.objects.all()
    datos = {
      'listaPerfilInstructor' : usuarioall2
    }
    return render(request,'app/listaperfilinstructor.html',datos)

#LISTAR DATOS PARA EL FUNCIONARIO
def listaperfilfuncionario(request):
    
    usuarioall3 = Usuariofuncionario.objects.all()
    datos = {
      'listaPerfilFuncionario' : usuarioall3
    }
    return render(request,'app/listaperfilfuncionario.html',datos)

#LISTAR DATOS PARA EL ADMIN
def listaperfiladmin(request):
    
    usuarioall4 = Usuarioadmin.objects.all()
    datos = {
      'listaPerfilAdmin' : usuarioall4
    }
    return render(request,'app/listaperfiladmin.html',datos)

#LISTAR DATOS PARA EL ADMIN
def listafunadmin(request):
    
    usuarioall4 = Usuariofuncionario.objects.all()
    datos = {
      'listaFunAdmin' : usuarioall4
    }
    return render(request,'app/listafunadmin.html',datos)

#LISTAR DATOS PARA EL ADMIN
def listarcuentashabilitadas(request):
    
   
    return render(request,'app/listarcuentashabilitadas.html')



#LISTAR DATOS PARA EL ADMIN
def listacuentahabi(request):
    
    usuarioall4 = Usuariofuncionario.objects.all()
    datos = {
      'listaFunAdmin' : usuarioall4
    }
    return render(request,'app/listafunadmin.html',datos)





#LISTAR ADULTO MAYOR PARA ADMINISTRAR DE ADMIN CRUD
@login_required
def listaraduladmin(request):
  usuarioadul= Usuario.objects.all()
  datos={
    'listarAdulAdmin':usuarioadul,
    

  }


  
  return render(request,'app/listaraduladmin.html',datos)
#TERMINA AQUI


#LISTAR INSTRUCTOR PARA ADMINISTRAR DE ADMIN CRUD
@login_required
def listarinstadmin(request):
  usuarioadul= Usuarioinstructor.objects.all()
  datos={
    'listarInstAdmin':usuarioadul,
    

  }


  
  return render(request,'app/listarinstadmin.html',datos)
#TERMINA AQUI

#LISTAR POSTULACIONES INSTRUCTOR PARA ADMINISTRAR DE EN FUNCIONARIO CRUD
@login_required
def listarpostulacion(request):
  usuarioall222= Postulacion.objects.all()
  datos={
    'listarPostulacion':usuarioall222,
    

  }


  
  return render(request,'app/listarpostulacion.html',datos)
#TERMINA AQUI

#LISTAR MATERIALES PARA ADMINISTRAR DE UN FUNCIONARIO CRUD
@login_required
def listarmateriales(request):
  usuarioall333= Materiales.objects.all()
  datos={
    'listarMateriales':usuarioall333,
    

  }


  
  return render(request,'app/listarmateriales.html',datos)
#TERMINA AQUI







#MODIFICAR A.MAYOR PERO DEL USUARIO ADMIN
@login_required
def modifiadultomayoradmin (request, run):
    usuario = Usuario.objects.get(run=run)
    datos = {
        'form' : UsuarioForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, files=request.FILES, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, '¡Modificación exitosa!')
            datos['form'] = formulario

    return render(request, 'app/modifiadultomayoradmin.html', datos)
#TERMINA AQUI

#MODIFICAR INSTRUCTOR PERO DEL USUARIO ADMIN
@login_required
def modifinstadmin (request, run):
    usuario = Usuarioinstructor.objects.get(run=run)
    datos = {
        'form' : UsuarioForminstructor(instance=usuario)
    }
    if request.method == 'POST':
        formulario = UsuarioForminstructor(data=request.POST, files=request.FILES, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, '¡Modificación exitosa!')
            datos['form'] = formulario

    return render(request, 'app/modifinstadmin.html', datos)
#TERMINA AQUI







#LISTAR Y CRUD DESDE EL FUNCIONARIO PARA TODOS LOS TIPOS DE USUARIO
#LISTAR ADULTO MAYOR PARA ADMINISTRAR DE FUNCIONARIO CRUD
@login_required
def listaradulfuncionario(request):
  usuarioadul= Usuario.objects.all()
  datos={
    'listarAdulFuncionario':usuarioadul,
    

  }


  
  return render(request,'app/listaradulfuncionario.html',datos)
#TERMINA AQUI


#CRUD ADULTO MAYOR PERO DESDE FUNCIONARIO
#MODIFICAR ADULTO MARYOR DE USUARIO FUNCIONARIO
@login_required
def modifiadultomayorfuncionario (request, run):
    usuario = Usuario.objects.get(run=run)
    datos = {
        'form' : UsuarioForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, files=request.FILES, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, '¡Modificación exitosa!')
            datos['form'] = formulario

    return render(request, 'app/modifiadultomayorfuncionario.html', datos)


#LISTAR DATOS INSTRUCTOR PARA MODIFICAR DE FUNCIONARIO CRUD
@login_required
def listarinsfuncionario(request):
  usuarioins=Usuarioinstructor.objects.all()
  datos={
  
    'listarInsFuncionario':usuarioins

  }


  
  return render(request,'app/listarinsfuncionario.html',datos)

#MODIFICAR INSTRUCTOR PERO DEL USUARIO FUNCIONARIO
@login_required
def modifinstructorfuncionario (request, run):
    usuario = Usuarioinstructor.objects.get(run=run)
    datos = {
        'form' : UsuarioForminstructor(instance=usuario)
    }
    if request.method == 'POST':
        formulario = UsuarioForminstructor(data=request.POST, files=request.FILES, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, '¡Modificación exitosa!')
            datos['form'] = formulario

    return render(request, 'app/modifinstructorfuncionario.html', datos)
#TERMINA AQUI


#FORMULARIO PARA REGISTRASE A LA PAGINA
def registro(request):
    datos = {
        'form' : RegistroUsuarioForm()
    }
    if request.method == 'POST':
        formulario = RegistroUsuarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            #user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            #login(request,user)
            messages.success(request,'Registrado correctamente!')
            #return redirect(to="home")
        datos["form"] = formulario

    return render(request, 'registration/register.html', datos)

#CARRITO DEL TALLER 
@login_required
def carritotaller(request):
  carritoTaller = ItemsTaller.objects.all()

  datos = {
    
    'listaTaller' : carritoTaller,
    
  }

  if request.method == 'POST':

    carritoTaller = ItemsTaller()
    carritoTaller.id = request.POST.get('id')
    carritoTaller.descripcionTaller=request.POST.get('descripcion')
    carritoTaller.delete()
    messages.success(request,'Taller eliminado!')
 

  return render (request, 'app/carritotaller.html', datos)

#MUESTRA TODOS LOS TALLERES AGREGADOS Y PUEDES INSCRIBIRTE, MAS API DIJIMON
@login_required
def talleres(request):



  response = requests.get('http://127.0.0.1:8000/api/talleres/').json()
  response2 = requests.get('https://digimon-api.vercel.app/api/digimon').json()
 
  
  talleresAll = Taller.objects.all()

  datos = {

    'listaTalleres' : talleresAll,
    'listaJson' : response,
    'listaDigimon': response2,

    

  }
    
  if request.method == 'POST':

    carritoTaller = ItemsTaller()
    carritoTaller.codigoTaller = request.POST.get('codigo')
    carritoTaller.nombreTaller = request.POST.get('nombre')
    carritoTaller.descripcionTaller = request.POST.get('descripcion')
    carritoTaller.imagen = request.POST.get('imagen')
    carritoTaller.save()
    messages.success(request,'Taller guardado!')



      

        

  return render(request,'app/talleres.html',datos)

#VISTA TALLERES EXCLUSIVA INSTRUCTOR
@login_required
def talleresinstructor(request):



  response = requests.get('http://127.0.0.1:8000/api/talleres/').json()
  response2 = requests.get('https://digimon-api.vercel.app/api/digimon').json()
 
  
  talleresAll = Taller.objects.all()

  datos = {

    'listaTalleres' : talleresAll,
    'listaJson' : response,
    'listaDigimon': response2,

    

  }
    
  if request.method == 'POST':

    carritoTaller = ItemsTaller()
    carritoTaller.codigoTaller = request.POST.get('codigo')
    carritoTaller.nombreTaller = request.POST.get('nombre')
    carritoTaller.descripcionTaller = request.POST.get('descripcion')
    carritoTaller.imagen = request.POST.get('imagen')
    carritoTaller.save()
   


      

        

  return render(request,'app/talleresinstructor.html',datos)


#VISTA TALLERES EXCLUSIVA FUNCIONARIO
def talleresfuncionario(request):



  response = requests.get('http://127.0.0.1:8000/api/talleres/').json()
  response2 = requests.get('https://digimon-api.vercel.app/api/digimon').json()
 
  
  talleresAll = Taller.objects.all()

  datos = {

    'listaTalleres' : talleresAll,
    'listaJson' : response,
    'listaDigimon': response2,

    

  }
    
  if request.method == 'POST':

    carritoTaller = ItemsTaller()
    carritoTaller.codigoTaller = request.POST.get('codigo')
    carritoTaller.nombreTaller = request.POST.get('nombre')
    carritoTaller.descripcionTaller = request.POST.get('descripcion')
    carritoTaller.imagen = request.POST.get('imagen')
    carritoTaller.save()
   


      

        

  return render(request,'app/talleresfuncionario.html',datos)


#VISTA TALLERES EXCLUSIVA ADMIN 
def talleresadmin(request):



  response = requests.get('http://127.0.0.1:8000/api/talleres/').json()
  response2 = requests.get('https://digimon-api.vercel.app/api/digimon').json()
 
  
  talleresAll = Taller.objects.all()

  datos = {

    'listaTalleres' : talleresAll,
    'listaJson' : response,
    'listaDigimon': response2,

    

  }
    
  if request.method == 'POST':

    carritoTaller = ItemsTaller()
    carritoTaller.codigoTaller = request.POST.get('codigo')
    carritoTaller.nombreTaller = request.POST.get('nombre')
    carritoTaller.descripcionTaller = request.POST.get('descripcion')
    carritoTaller.imagen = request.POST.get('imagen')
    carritoTaller.save()
   


      

        

  return render(request,'app/talleresadmin.html',datos)







#MODIFICAR LOS TALLERES DEL FUNCIONARIO
@login_required
def modificartalleres (request, codigo):
    taller = Taller.objects.get(codigo=codigo)
    datos = {
        'form' : TallerForm(instance=taller)
    }
    if request.method == 'POST':
        formulario = TallerForm(data=request.POST, files=request.FILES, instance=taller)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, '¡Modificación exitosa!')
            datos['form'] = formulario

    return render(request, 'app/modificartalleres.html', datos)

#MODIFICAR LOS TALLERES DEL ADMIN
@login_required
def modificartalleradmin (request, codigo):
    taller = Taller.objects.get(codigo=codigo)
    datos = {
        'form' : TallerForm(instance=taller)
    }
    if request.method == 'POST':
        formulario = TallerForm(data=request.POST, files=request.FILES, instance=taller)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, '¡Modificación exitosa!')
            datos['form'] = formulario

    return render(request, 'app/modificartalleradmin.html', datos)



#ELIMINA CUALQUIER TALLER
@login_required
def quitar(request, id):

  carritoTaller = ItemsTaller.objects.get(id=id)
  carritoTaller.delete()
  messages.success(request,'Taller eliminado!')

  return redirect(to="carritotaller")
  