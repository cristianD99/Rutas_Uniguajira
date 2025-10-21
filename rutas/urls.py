from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('reservar/', views.reservar, name='reservar'),
]
