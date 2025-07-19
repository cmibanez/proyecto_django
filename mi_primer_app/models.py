# C:\Users\ciban\OneDrive\Escritorio\Cursos\Python\DJANGO\ejemplo_django\mi_primer_app\models.py

from django.db import models

class Familiar(models.Model): # Clases van con mayúscula inicial por convención (ej. Familiar en vez de familiar)
    nombre = models.CharField(max_length=50) # CORREGIDO: max_length
    apellido = models.CharField(max_length=50)
    parentesco = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()

    def __str__(self): # CORREGIDO: espacio entre def y __str__
        # Asegúrate de que esta línea sea válida, si self.apellido no existe, bórralo.
        # Además, self,apellido tiene una coma en vez de un punto.
        # Corregí para que la f-string sea más legible y correcta.
         return f"{self.nombre} {self.apellido} ({self.parentesco}) - Edad: {self.edad}, Nacido el: {self.fecha_nacimiento}"
    

