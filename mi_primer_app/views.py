from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request,'mi_primer_app/inico.html')

def saludo(request):
    return HttpResponse("Hola, mundo!")
def saludo_con_template(request):
    return render (request,'mi_primer_app/saludo.html')


def crear_familiar (request, nombre):
    if nombre is not None:

        nuevo_familiar= familiar (
            nombre=nombre,
            apellido="ApellidoEjemplo",
            edad=30,
            fecha_nacimiento=-"1993-01-01",
            parentesco="Primo"
        )
        nuevo_familiar.save()
    return render (request, "mi_primer_app/templates/templates/crear_familiar.html", {"nombre": nombre})
