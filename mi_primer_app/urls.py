from django.urls import path # Correcta importación de 'path' desde Django
from .views import saludo, saludo_con_template, crear_familiar, inicio, crear_curso        # Importa el módulo 'views' de tu propia aplicación

urlpatterns = [
    path('', inicio, name='inicio'),
    path ('hola-mundo/', saludo),
    path('Hola, mundo!-template/', saludo_con_template),
    path ('crear_familiar/<str:nombre>/', crear_familiar),
    path ('crear_curso/', crear_curso, name='crear-curso'),
               ]
