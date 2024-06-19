from django.urls import path
from . import views





urlpatterns = [
    path('', views.Vista_Blog, name="Blog"),
    path('categoria/<int:categoria_id>/', views.Categoria, name = "categoria"),
    
    
]




