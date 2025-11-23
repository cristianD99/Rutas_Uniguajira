from django.urls import  path
from . import views
from .views import login_admin



 

urlpatterns = [
    path('', views.index, name='index'),                          
    path('admin-login/', login_admin, name='login_admin'), 
    path('registrar_usuario/', views.registrarme, name='registrar_usuario'),
    path('login/', views.login_usuario, name='login_usuario'),
    path('log', views.log, name='inicio'),
    path('reservar/', views.reservar, name='reservar'),
    path('resrvar_puesto/', views.reservar_puesto, name='reservar_puesto'),
    path('ajax/cargar_paradas/', views.cargar_paradas, name='ajax_cargar_paradas'), 
    path('comprobante/<int:reserva_id>/', views.comprobante, name='comprobante'),

]
