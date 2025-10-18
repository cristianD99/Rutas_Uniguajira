from django.db import models
from estudiantes.models import Estudiante
from rutas.models import Ruta

class Reserva(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    asiento = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.estudiante.nombre} - {self.ruta.nombre} ({self.fecha})"
