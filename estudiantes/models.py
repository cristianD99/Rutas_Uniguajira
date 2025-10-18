from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    codigo = models.CharField(max_length=20)
    programa = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
