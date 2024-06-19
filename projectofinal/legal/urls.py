from django.urls import path
from . import views

urlpatterns = [
    path('legal/', views.aviso_legal, name='legal'),
    # otras rutas...
]
