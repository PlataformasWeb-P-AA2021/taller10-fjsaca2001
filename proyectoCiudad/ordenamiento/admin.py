from django.contrib import admin

# Register your models here.


from ordenamiento.models import *
class ParroquiaAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str)
    # de la clase
    list_display = ('nombre', 'tipo')
    search_fields = ('nombre', 'tipo')

# admin.site.register se lo altera
# el primer argumento es el modelo (Parroquia)
# el segundo argumento la clase ParroquiaAdmin
#
admin.site.register(Parroquia, ParroquiaAdmin)


class BarrioAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str)
    # de la clase
    list_display = ('nombre', 'nroViviendas', 'nroParques', 'nroEdificios', 'parroquia')
    # se agrega el atributo
    # raw_id_fields que permite acceder a una interfaz
    # para buscar los estudiantes y seleccionar el que
    # se desee
    raw_id_fields = ('parroquia',)

admin.site.register(Barrio, BarrioAdmin)