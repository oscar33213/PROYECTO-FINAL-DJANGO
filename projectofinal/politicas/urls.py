from django.urls import path
from . import views

urlpatterns = [
    path('politicas/', views.politicas, name='politicas'),
    # otras rutas...
]
