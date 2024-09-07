from django.db import models
from django.contrib.auth.models import User
from proyectos.models import Proyecto

from django.db import models
from django.contrib.auth.models import User
from proyectos.models import Proyecto

class Tarea(models.Model):
    PRIORIDADES_TAREA = [
        ('B', 'Baja'),
        ('M', 'Media'),
        ('A', 'Alta'),
    ]

    ESTADOS_TAREA = [
        ('P', 'Pendiente'),
        ('E', 'En progreso'),
        ('C', 'Completada'),
    ]

    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    asignado_a = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField()  # Cambiado a DateTimeField para registrar fecha y hora
    fecha_fin = models.DateTimeField()  # Cambiado a DateTimeField para registrar fecha y hora
    prioridad = models.CharField(
        max_length=1,
        choices=PRIORIDADES_TAREA,
        default='M'
    )
    estado = models.CharField(
        max_length=1,
        choices=ESTADOS_TAREA,
        default='P'
    )

    def __str__(self):
        return self.nombre



class ComentarioTarea(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.usuario} en {self.tarea}"

