from django.db import models
from proyectos.models import Proyecto

class Recurso(models.Model):
    TIPO_RECURSO = [
        ('material', 'Material'),
        ('equipo', 'Equipo'),
        ('personal', 'Personal'),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=TIPO_RECURSO)
    cantidad = models.PositiveIntegerField()
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    fecha_asignacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - {self.proyecto.nombre}"
