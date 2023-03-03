from django.contrib import admin
from .models import *

class AdminAuto (admin.ModelAdmin):
  list_display = ["_str_", "placa"]
  class Meta(object):
    model:Auto

class AdminPropietario(admin.ModelAdmin):
  list_display = ["_str_","nombre","apellido", "cedula", "idAuto"]
  class Meta(object):
    model:Propietario


admin.site.register(Auto)
admin.site.register(Propietario)
