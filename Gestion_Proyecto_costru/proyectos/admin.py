from django.contrib import admin
from .models import Equipo,Proyecto,MiembroEquipo
# Register your models here.


admin.site.register(MiembroEquipo),
admin.site.register(Equipo),
admin.site.register(Proyecto),
