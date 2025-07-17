from django.db import models

# Create your models here.
class familiar(models.Model):
    nombre = models.CharField(max_lenght=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    parentesco = models.CharField (max_length=50)

    def__str__(self):
        return f"{self.nombre}{self,apellido}({self.parentesco})- Edad:{self.edad}, Nacido el:{self.fecha_nacimiento}"

