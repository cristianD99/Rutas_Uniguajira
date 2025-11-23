from django import forms
from .models import PerfilUsuario
from .models import Ruta, Parada, HorarioRuta, Reserva

class PerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ['nombre', 'correo', 'contraseña']  

        from django import forms


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nombre_usuario', 'ruta', 'parada', 'horario']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
     
        self.fields['parada'].queryset = Parada.objects.none()

        if 'ruta' in self.data:
            try:
                ruta_id = int(self.data.get('ruta'))
                self.fields['parada'].queryset = Parada.objects.filter(ruta_id=ruta_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['parada'].queryset = self.instance.ruta.paradas