from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import PerfilUsuario
from .forms import ReservaForm
from .models import Parada
import random
from .models import Ruta



usuarios = []  


def registrarme(request):
    mensaje = ""
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        contraseña = request.POST.get('contraseña')

        if nombre and correo and contraseña:
            
            PerfilUsuario.objects.create(nombre=nombre, correo=correo, contraseña=contraseña)
            mensaje = "✅ Usuario registrado correctamente"
        else:
            mensaje = "⚠️ Todos los campos son obligatorios"

    return render(request, 'registrar_usuario.html', {'mensaje': mensaje})

def login_usuario(request):

    
    mensaje = ""
    if request.method == "POST":
        correo = request.POST.get("correo")
        contraseña = request.POST.get("contraseña")
        try:
            usuario = PerfilUsuario.objects.get(correo=correo, contraseña=contraseña)
           
            request.session['usuario_id'] = usuario.id
            request.session['usuario_nombre'] = usuario.nombre
            return redirect('reservar_puesto')  
        except PerfilUsuario.DoesNotExist:
            mensaje = "Correo o contraseña incorrectos"
    return render(request, "rutas/log.html", {"mensaje": mensaje})



def index(request):
    return render(request, 'index.html')


def cargar_paradas(request):
    ruta_id = request.GET.get('ruta')
    paradas = Parada.objects.filter(ruta_id=ruta_id).order_by('nombre')
    return JsonResponse(list(paradas.values('id', 'nombre')), safe=False)

def log(request):
    return render(request, 'log.html')


def login_admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff: 
            login(request, user)
            return redirect('/admin/')  
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')

    return render(request, 'login_admin.html')



def reservar(request):
    
    return render(request, 'reservar.html')



def reservar_puesto(request):

     
    if not request.session.get('usuario_id'):
        return redirect('login_usuario')

    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.usuario_id = request.session['usuario_id']
            reserva.puesto = random.randint(1, 42)
            reserva.save()
            return render(request, 'comprobante.html', {'reserva': reserva})
    else:
        form = ReservaForm()  

    return render(request, 'rutas/reservar_puesto.html', {'form': form})
    
    


def comprobante(request, reserva_id):

    from .models import Reserva 
    try:
        reserva = Reserva.objects.get(id=reserva_id)
    except Reserva.DoesNotExist:
        return HttpResponse("Reserva no encontrada", status=404)

    return render(request, "comprobante.html", {"reserva": reserva})
