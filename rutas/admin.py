from django.contrib import admin
from .models import PerfilUsuario  
from .models import Ruta, Parada, HorarioRuta, Reserva


admin.site.register(Ruta)
admin.site.register(Parada)
admin.site.register(HorarioRuta)
admin.site.register(Reserva)
admin.site.register(PerfilUsuario)

class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'programa')
    search_fields = ('nombre', 'correo')


class ParadaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ruta')  
    actions = ['delete_selected']
