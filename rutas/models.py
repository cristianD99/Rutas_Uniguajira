from django.db import models
from datetime import time, date

class Ruta(models.Model):
    OPCIONES_RUTA = [
        ('Centro_Coquivacoa', 'Centro - Coquivacoa'),
        ('Majayura', 'Majayura'),
        ('Marbella', 'Marbella'),
        ('La20', 'La 20'),
        ('15deMayo', '15 de Mayo'),
        ('27_37', '27-37'),
        ('15Derecho', '15 Derecho'),
        ('Dividivi', 'Dividivi'),
        ('RoundPoint', 'Round Point'),
    ]

    nombre = models.CharField(
        max_length=100,
        choices=OPCIONES_RUTA,
        unique=True
    )
    capacidad = models.PositiveIntegerField(default=40)

    def __str__(self):
        return self.get_nombre_display()


class HorarioRuta(models.Model):
    DIAS_SEMANA = [
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
    ]

    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE, related_name='horarios')
    dia = models.CharField(max_length=20, choices=DIAS_SEMANA)
    fecha = models.DateField()  # ✅ Nuevo campo para la fecha
    hora = models.TimeField()   # ✅ Nuevo campo para la hora principal
    hora_salida = models.TimeField()
    hora_llegada = models.TimeField()

    def __str__(self):
        return (
            f"{self.ruta.get_nombre_display()} - {self.dia} "
            f"{self.fecha.strftime('%d/%m/%Y')} "
            f"({self.hora_salida.strftime('%H:%M')} → {self.hora_llegada.strftime('%H:%M')})"
        )
