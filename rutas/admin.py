from django.contrib import admin
from .models import Ruta, HorarioRuta  # ✅ Cambia Reserva por HorarioRuta

admin.site.register(Ruta)
admin.site.register(HorarioRuta)
