from django.urls import path
from proyectowebapp import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.Vista_Home, name="Home"),
    
    
    
    
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)