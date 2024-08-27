from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    Tareas_usuario = models.CharField(max_length=30, blank=True)
    fecha_ingreso = models.DateField(null=True, blank=True)
    

    def __str__(self):
        return self.user.username




