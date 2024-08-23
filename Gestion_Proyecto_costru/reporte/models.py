from django.db import models

class Reporte(models.Model):
    titulo = models.CharField(max_length=100)
    fecha_creacion = models.DateField(auto_now_add=True)
    tipo = models.CharField(max_length=50)  # Ejemplo: "Progreso", "Desempeño"
    descripcion = models.TextField()
    archivo = models.FileField(upload_to='reportes/')  # Si quieres generar archivos PDF/Excel

    def __str__(self):
        return self.titulo
