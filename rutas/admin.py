from django.contrib import admin
from .models import Ruta

@admin.register(Ruta)
class RutaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'origen', 'destino', 'horario')
    search_fields = ('nombre', 'origen', 'destino')
