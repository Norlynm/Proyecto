from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from tareas.models import Tarea
# Create your models here.



class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    Tareas_usuario = models.ForeignKey(Tarea, max_length=30, blank=True,on_delete=models.CASCADE)
    fecha_ingreso = models.DateField()
    

    def __str__(self):
        return self.user.username




