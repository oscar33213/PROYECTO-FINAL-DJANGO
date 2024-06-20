from django.shortcuts import render
from .models import Fotos
# Create your views here.


def galeria(request):
    fotos = Fotos.objects.all()
    return render(request, 'galeria/galeria.html', {'fotos':fotos})