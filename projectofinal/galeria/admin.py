from django.contrib import admin
from .models import Fotos
# Register your models here.


class FotosAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    
    
    
admin.site.register(Fotos, FotosAdmin)