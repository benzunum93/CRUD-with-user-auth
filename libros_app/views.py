from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm
# Create your views here.

def inicio(request):
    return render( request, 'pagina/inicio.html')

def marco_libreria(request):
    return render( request, 'pagina/marco_html.html')
def index_libreria(request):

    libros= Libro.objects.all()
    return render( request, 'pagina/index.html', { 'libros':libros})


def crear_libreria(request):

    formulario= LibroForm(request.POST or None, request.FILES or None)

    if formulario.is_valid():
        formulario.save() #Guarda los datos

        return  redirect('/libros')
    return render( request, 'pagina/crear.html', {'formulario':formulario})


def editar_libreria(request, id):
    libros=Libro.objects.get(id=id)
    formulario= LibroForm(request.POST or None, request.FILES or None, instance=libros)

    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('/libros')
    return render( request, 'pagina/update.html', {'formulario':formulario})


def eliminar_libreria(request, id):

    libros=Libro.objects.get(id=id)

    libros.delete()
    return redirect('/libros')

