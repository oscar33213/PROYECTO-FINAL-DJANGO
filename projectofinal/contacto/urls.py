from django.urls import path
from . import views




urlpatterns = [
    path('', views.Vista_Contacto, name= "Contacto"),
    
    
]


