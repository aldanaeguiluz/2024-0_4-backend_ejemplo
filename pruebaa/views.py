from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pruebaEndpoint(request):
    return HttpResponse("Esto es una prueba")

def nuevoEndpoint(request):
    return HttpResponse("<h1>Nuevo!!</h1>")