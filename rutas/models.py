from django.db import models
import random



class PerfilUsuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    contraseña = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
class Ruta(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Parada(models.Model):
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE, related_name="paradas")
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.ruta.nombre} - {self.nombre}"


class HorarioRuta(models.Model):
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    hora = models.TimeField()

    def __str__(self):
        return f"{self.ruta.nombre} - {self.hora}"


class Reserva(models.Model):
    nombre_usuario = models.CharField(max_length=100)
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    parada = models.ForeignKey(Parada, on_delete=models.CASCADE)
    horario = models.ForeignKey(HorarioRuta, on_delete=models.CASCADE)

    puesto = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.puesto:
            self.puesto = random.randint(1, 42)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre_usuario} - {self.ruta.nombre} - Puesto {self.puesto}"