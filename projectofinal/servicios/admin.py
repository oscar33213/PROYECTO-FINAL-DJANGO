from django.contrib import admin
from .models import Servicio

# Register your models here.
class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') #INDICAMOS QUE ESTOS CAMPOS SOLO SERAN LECTURA
    
admin.site.register(Servicio, ServicioAdmin)

