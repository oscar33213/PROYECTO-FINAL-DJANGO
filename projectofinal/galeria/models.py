from django.db import models

# Create your models here.


class Fotos(models.Model):
    titulo = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='galeria')
    pieFoto = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        verbose_name= 'foto'
        verbose_name_plural = 'fotos'
        
    def __str__(self):
        return self.titulo