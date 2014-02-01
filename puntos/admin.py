from django.contrib import admin
from .models import Persona, Rol, Genero
# Register your models here.

admin.site.register(Persona)
admin.site.register(Rol)
admin.site.register(Genero)