from django.urls import path
from . import views

urlpatterns = [
    path('registrarDetenido', views.registrarDetenido, name='resgistrarDetenido'),
    path('gestionarPolicia', views.gestionarPolicia, name='gestionarPolicia'),
    path('modificarInformacion', views.modificarInformacion, name='modificarInformacion'),
    path('registrarPolicia', views.registrarPolicia, name='registrarPolicia'),
    path ('menu', views.menu, name='menu'),
    path('gestionarDetenidos', views.gestionarDetenidos, name='gestionarDetenidos'),
    path('visualizarInformacion', views.visualizarInformacion, name='visualizarInformacion'),
    path('iniciarSesion', views.iniciarSesion, name='iniciarSesion'),
]