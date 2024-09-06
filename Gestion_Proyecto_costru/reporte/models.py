from django.db import models
from proyectos.models import Proyecto
from tareas.models import Tarea
from django.contrib.auth.models import User
class Reporte(models.Model):
    titulo = models.CharField(max_length=100)
    fecha_creacion = models.DateField(auto_now_add=True)
    tipo = models.CharField(max_length=50)  # Ejemplo: "Progreso", "Desempeño"
    descripcion = models.TextField()
    archivo = models.FileField(upload_to='Reporte/')  # Si quieres generar archivos PDF/Excel
    tareas = models.ManyToManyField(Tarea, blank=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    reporte = models.ForeignKey(Reporte, related_name="comentarios", on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario por {self.usuario.username} en {self.reporte.titulo}"