from django.contrib import admin
from .models import Tarea,ComentarioTarea
# Register your models here.

admin.site.register(Tarea),
admin.site.register(ComentarioTarea)