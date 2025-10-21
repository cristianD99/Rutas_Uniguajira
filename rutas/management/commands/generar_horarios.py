from django.core.management.base import BaseCommand
from rutas.models import Ruta, HorarioRuta
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = "Genera horarios automáticos (5am - 10pm, cada hora, descansos 8am, 2pm y 8pm)"

    def handle(self, *args, **kwargs):
        dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
        hora_inicio = datetime.strptime("05:00", "%H:%M")
        hora_fin = datetime.strptime("22:00", "%H:%M")
        descansos = ["08:00", "14:00", "20:00"]

        rutas = Ruta.objects.all()
        if not rutas.exists():
            self.stdout.write(self.style.WARNING("⚠️ No hay rutas registradas. Agrega rutas antes de generar horarios."))
            return

        for ruta in rutas:
            for dia in dias:
                hora = hora_inicio
                while hora <= hora_fin:
                    hora_str = hora.strftime("%H:%M")
                    if hora_str not in descansos:
                        salida = hora.time()
                        llegada = (hora + timedelta(minutes=30)).time()
                        HorarioRuta.objects.get_or_create(
                            ruta=ruta,
                            dia=dia,
                            hora_salida=salida,
                            hora_llegada=llegada
                        )
                    hora += timedelta(hours=1)

        self.stdout.write(self.style.SUCCESS("✅ Horarios generados correctamente para todas las rutas."))
