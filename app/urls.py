from operator import index
from unicodedata import name
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('index/', index, name='index'),
  path('usuarioform/',usuarioform ,name= "usuarioform"),
  path('usuarioforminstructor/',usuarioforminstructor ,name= "usuarioforminstructor"),
  path('usuarioformfuncionario/',usuarioformfuncionario ,name= "usuarioformfuncionario"),
  path('usuarioformadmin/',usuarioformadmin ,name= "usuarioformadmin"),
  path('reporte/',reporte ,name= "reporte"),
  path('postulacionform/',postulacionform,name= "postulacionform"),
  path('listarpostulacion/',listarpostulacion ,name= "listarpostulacion"),
  path('modifipostulacion/<codigo>',modifipostulacion ,name= "modifipostulacion"),
  path('eliminarpostulacion/<codigo>',eliminarpostulacion ,name= "eliminarpostulacion"),
  path('materialesform/',materialesform ,name= "materialesform"),
  path('listarmateriales/',listarmateriales ,name= "listarmateriales"),
  path('modifimate/<codigo>',modifimate ,name= "modifimate"),
  path('eliminarmate/<codigo>',eliminarmate ,name= "eliminarmate"),
  path('usuarioformfunadmin/',usuarioformfunadmin ,name= "usuarioformfunadmin"),
  path('usuarioformaduladmin/',usuarioformaduladmin ,name= "usuarioformaduladmin"),
  path('usuarioforminstadmin/',usuarioforminstadmin ,name= "usuarioformintsadmin"),
  path('registro/', registro, name='registro'),
  path('nosotros/', nosotros, name='nosotros'),
  path('agregartaller/', agregartaller, name='agregartaller'),
  path('agregartalleradmin/', agregartalleradmin, name='agregartalleradmin'),
  path('modificartalleradmin/<codigo>',modificartalleradmin, name='modificartalleradmin'),
  path('carritotaller/', carritotaller, name='carritotaller'),
  path('quitar/<id>', quitar, name='quitar'), 
  path('talleres/', talleres, name='talleres'),
  path('talleresinstructor/', talleresinstructor, name='talleresinstructor'),
  path('talleresfuncionario/', talleresfuncionario, name='talleresfuncionario'),
  path('talleresadmin/', talleresadmin, name='talleresadmin'),
  path('listaperfil/',listaperfil ,name= "listaperfil"),
  path('modifiadultomayor/<run>',modifiadultomayor ,name= "modifiadultomayor"),
  path('eliminaradultomayor/<run>',eliminaradultomayor ,name= "eliminaradultomayor"),
  path('listaperfilinstructor/',listaperfilinstructor ,name= "listaperfilinstructor"),
  path('modifinstructor/<run>',modifinstructor ,name= "modifinstructor"),
  path('eliminarinstructor/<run>',eliminarinstructor ,name= "eliminarinstructor"),
  path('listaperfilfuncionario/',listaperfilfuncionario ,name= "listaperfilfuncionario"),
  path('modififuncionario/<run>',modififuncionario ,name= "modififuncionario"),
  path('eliminarfuncionario/<run>',eliminarfuncionario ,name= "eliminarfuncionario"),
  path('listaperfiladmin/',listaperfiladmin ,name= "listaperfiladmin"),
  path('modifiadmin/<run>',modifiadmin ,name= "modifiadmin"),
  path('eliminaradmin/<run>',eliminaradmin ,name= "eliminaradmin"),
  path('listafunadmin/',listafunadmin ,name= "listafunadmin"),
  path('listarcuentashabilitadas/',listarcuentashabilitadas ,name= "listarcuentashabilitadas"),
  path('modififunadmin/<run>',modififunadmin ,name= "modififunadmin"),
  path('eliminarfunadmin/<run>',eliminarfunadmin ,name= "eliminarfunadmin"),
  path('eliminartaller/<codigo>',eliminartaller ,name= "eliminartaller"),
  path('modificartalleres/<codigo>',modificartalleres ,name= "modificartalleres"),
  path('caliestrellas',caliestrellas ,name= "caliestrellas"),
  path('pagos',pagos ,name= "pagos"),
  path('listaradulfuncionario',listaradulfuncionario ,name= "listaradulfuncionario"),
  path('modifiadultomayorfuncionario/<run>',modifiadultomayorfuncionario ,name= "modifiadultomayorfuncionario"),
  path('listarinsfuncionario',listarinsfuncionario ,name= "listarinsfuncionario"),
  path('modifinstructorfuncionario/<run>',modifinstructorfuncionario ,name= "modifinstructorfuncionario"),
  path('listaraduladmin',listaraduladmin,name= "listaraduladmin"),
  path('modifiadultomayoradmin/<run>',modifiadultomayoradmin ,name= "modifiadultomayoradmin"),
  path('listarinstadmin',listarinstadmin,name= "listarinstadmin"),
  path('modifinstadmin/<run>',modifinstadmin ,name= "modifinstadmin"),


  

]   

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)