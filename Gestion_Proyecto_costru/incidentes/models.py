from django.db import models
from proyectos.models import Proyecto
from django.contrib.auth.models import User

class Incidente(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha = models.DateField() 
    responsable = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    estado = models.CharField(max_length=50, choices=[('pendiente', 'Pendiente'), ('resuelto', 'Resuelto')])

    def __str__(self):
        return f"Incidente en {self.proyecto.nombre} - {self.estado}"
