from django.urls import path # Correcta importación de 'path' desde Django
from . import views         # Importa el módulo 'views' de tu propia aplicación

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path ("Hola, mundo!",views.saludo),
    path('Hola, mundo!-template/',views.saludo_con_template),
    path ('crear-familiar/<str:nombre>',views.crear_familiar),
               
               ]
