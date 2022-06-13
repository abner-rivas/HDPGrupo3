import re
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def registrarDetenido(request):
    return render(request, 'paginas/registrarDetenido.html')

def gestionarPolicia(request):
    return render(request, 'paginas/gestionarPolicia.html')

def modificarInformacion(request):
    return render(request, 'paginas/modificarInformacion.html')

def registrarPolicia(request):
    return render(request, 'paginas/registrarPolicia.html')

def menu(request):
    return render(request, 'paginas/menu.html')

def gestionarDetenidos(request):
    return render(request, 'paginas/gestionarDetenidos.html')

def visualizarInformacion(request):
    return render(request, 'paginas/visualizarInformacion.html')

def iniciarSesion(request):
    return render(request, 'paginas/iniciarSesion.html')