
from .views import path

from .views import saludo, saludo_con_template, crear_familiar

urlpatterns = [path ('Hola, mundo!',saludo),
               path('Hola, mundo!-template/',saludo_con_template),
               path ('crear-familiar/<str:nombre>',crear_familiar),
               
               ]
