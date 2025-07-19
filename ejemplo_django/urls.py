from django.contrib import admin
from django.urls import path, include # Asegúrate de que 'include' también esté importado aquí

urlpatterns = [
    path('admin/', admin.site.urls),
    # Esta línea enlaza las URLs de tu aplicación 'mi_primer_app'
    # bajo la ruta 'mi-primer-app/'.
    path('mi-primer-app/', include('mi_primer_app.urls')),
]

