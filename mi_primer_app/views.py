from django.http import HttpResponse
from django.shortcuts import render
from .models import Familiar

from .forms import CursoForm

# Create your views here.

def inicio(request):    return render(request,'mi_primer_app/templates/inicio.html')

def saludo(request):
    return HttpResponse('Hola, mundo!')

def saludo_con_template(request):
    return render (request,'mi_primer_app/templates/saludo.html')

def crear_familiar (request, nombre):
    if nombre is not None:

        nuevo_familiar= Familiar (
            nombre=nombre,
            apellido="ApellidoEjemplo",
            edad=30,
            fecha_nacimiento="1993-01-01",
            parentesco="Primo"
        )
        nuevo_familiar.save()
    return render (request, 'mi_primer_app/templates/crear_familiar.html', {"nombre": nombre})

def crear_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            # Procesar el formulario y guardar el curso
            form.save()
        return render(request, "mi_primer_app/curso_creado.html", {"form": form})