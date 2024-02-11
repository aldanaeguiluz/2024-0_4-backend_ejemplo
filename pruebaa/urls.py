from django.urls import path
from pruebaa.views import pruebaEndpoint, nuevoEndpoint

urlpatterns=[
    path("hola", pruebaEndpoint),
    path("nuevo", nuevoEndpoint)
]