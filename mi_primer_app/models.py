# C:\Users\ciban\OneDrive\Escritorio\Cursos\Python\DJANGO\ejemplo_django\mi_primer_app\models.py

from django.db import models

class Familiar(models.Model): # Clases van con mayúscula inicial por convención (ej. Familiar en vez de familiar)
    nombre = models.CharField(max_length=50) # CORREGIDO: max_length
    apellido = models.CharField(max_length=50)
    parentesco = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()

    def __str__(self):
         return f"{self.nombre} {self.apellido} ({self.parentesco}) - Edad: {self.edad}, Nacido el: {self.fecha_nacimiento}"
    

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    duracion_semanas = models.IntegerField(default=4)
    fecha_inicio = models.DateField()
    activo = models.BooleanField(default=True)

    def _str_(self):
        return self.nombre