from django.contrib import admin

from app.views import  registro, usuarioform 
from .models import *

class TallerAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','tipo','descripcion', 'imagen','created_at','updated_at']
    search_fields = ['codigo']
    list_per_page = 4

class ReporteAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','descripcion', 'imagen','created_at','updated_at']
    search_fields = ['codigo']
    list_per_page = 8

class PostulacionAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','descripcion', 'imagen','created_at','updated_at']
    search_fields = ['codigo']
    list_per_page = 8

class MaterialesAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','descripcion', 'imagen','created_at','updated_at']
    search_fields = ['codigo']
    list_per_page = 9


class ItemsTallerAdmin(admin.ModelAdmin):
    list_display = ['id','nombreTaller','imagen']
    search_fields = ['id', 'nombreTaller']
    list_per_page = 3

class UsuarioAdmin(admin.ModelAdmin):
    list_display=['run','nombre','apellido','comuna','correo','telefono','imagen','updated_at']
    search_fields=['run']
    list_per_page=6

class UsuarioinstructorAdmin(admin.ModelAdmin):
    list_display=['run','nombre','apellido','comuna','correo','telefono','imagen','updated_at']
    search_fields=['run']
    list_per_page=5

class UsuariofuncionarioAdmin(admin.ModelAdmin):
    list_display=['run','nombre','apellido','comuna','correo','telefono','imagen','updated_at']
    search_fields=['run']
    list_per_page=7


admin.site.register(TipoTaller)
admin.site.register(Taller, TallerAdmin)
admin.site.register(ItemsTaller,ItemsTallerAdmin)
admin.site.register(Reporte,ReporteAdmin)
admin.site.register(Postulacion,PostulacionAdmin)
admin.site.register(Materiales,MaterialesAdmin)
admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Usuarioinstructor,UsuarioinstructorAdmin)
admin.site.register(Usuariofuncionario,UsuariofuncionarioAdmin)
