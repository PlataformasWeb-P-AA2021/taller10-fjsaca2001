from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

# importar las clases de models.py
from ordenamiento.models import Barrio, Parroquia

# importar los formularios de forms.py
from ordenamiento.forms import ParroquiaForm, BarrioForm, BarrioParroquiaForm

# Create your views here.

def index (request):
    """
        Listar los registros de parroquia y sus barrios.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # parroquias
    parroquia = Parroquia.objects.all()
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'parroquias': parroquia}
    return render(request, 'index.html', informacion_template)

def listarBarrios (request):
    """
            Listar los registros de barrios.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # barrios
    barrios = Barrio.objects.all()
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'barrios': barrios}
    return render(request, 'listarBarrios.html', informacion_template)

def agregarParroquia (request):
    """
    """
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'agregarParroquia.html', diccionario)

def agregarBarrio (requests):
    """
    """
    if requests.method=='POST':
        formulario = BarrioForm(requests.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm()
    diccionario = {'formulario': formulario}

    return render(requests, 'agregarBarrio.html', diccionario)

def editarParroquia (request, id):
    """
    """
    parroquia = Parroquia.objects.get(pk=id)
    if request.method == 'POST':
        formulario = ParroquiaForm(request.POST, instance=parroquia)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm(instance=parroquia)
    diccionario = {'formulario': formulario}

    return render(request, 'editarParroquia.html', diccionario)

def editarBarrio(request, id):
    """
    """
    barrio = Barrio.objects.get(pk=id)
    if request.method == 'POST':
        formulario = BarrioForm(request.POST, instance=barrio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm(instance=barrio)
    diccionario = {'formulario': formulario}

    return render(request, 'editarBarrio.html', diccionario)

def agregarBarrioParroquia(request, id):
    """
    """
    parroquia = Parroquia.objects.get(pk=id)
    if request.method == 'POST':
        formulario = BarrioParroquiaForm(parroquia, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioParroquiaForm(parroquia)
    diccionario = {'formulario': formulario, 'parroquia': parroquia}

    return render(request, 'agregarBarrioParroquia.html', diccionario)