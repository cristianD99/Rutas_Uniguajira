from django.db import models

class Ruta(models.Model):
    nombre = models.CharField(max_length=100)
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    horario = models.TimeField()

    def __str__(self):
        return f"{self.nombre} ({self.origen} → {self.destino})"
