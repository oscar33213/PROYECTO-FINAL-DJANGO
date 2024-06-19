from django.shortcuts import render
from servicios.models import Servicio

# Create your views here.

def Vista_Servicios(request):
     servicios = Servicio.objects.all() #IMPORTAMOS TODOS LOS OBJETOS DENTRO DE LA CLASE "SERVICIO (LA BASE DE DATOS)"
     return render (request, 'servicios/servicios.html', {"servicios": servicios})