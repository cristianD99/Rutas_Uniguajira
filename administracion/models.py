from django.db import models # type: ignore

# Create your models here.
from django.db import models # type: ignore

class Conductor(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=15, unique=True)
    telefono = models.CharField(max_length=15)
    licencia = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} - {self.licencia}"
