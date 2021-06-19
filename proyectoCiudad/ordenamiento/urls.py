"""
    Manejo de urls para la aplicación
    ordenamiento
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('barrios', views.listarBarrios, name='barrios'),
    path('agregar/parroquia', views.agregarParroquia, name='agregarParroquia'),
    path('agregar/barrio', views.agregarBarrio, name='agregarBarrio'),
    path('agregar/barrio/parroquia/<int:id>', views.agregarBarrioParroquia, name='agregarBarrioParroquia'),
    path('editar/parroquia/<int:id>', views.editarParroquia, name='editarParroquia'),
    path('editar/barrio/<int:id>', views.editarBarrio, name='editarBarrio'),
]
