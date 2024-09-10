from django.db import models
from django.contrib.auth.models import User

# Modelo para representar un equipo.
class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    usuarios = models.ManyToManyField(User)
    
    def __str__(self) :
        return f"{self.nombre}" # Devuelve el nombre del equipo cuando se imprime el objeto.
    

     
# proyectos/models.py

class Proyecto(models.Model):

    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    ESTADOS = [ 
            ('P','Pendiente'),
            ('E','En progreso'),        
            ('C','Completado'),
            ]
    estado=models.CharField(max_length=1,choices=ESTADOS,default='P')
    equipo = models.ForeignKey('Equipo', on_delete=models.CASCADE) # Relación con el equipo, borra el proyecto si el equipo se borra.
    equipo = models.ManyToManyField(User, related_name='proyectos')
    
    def __str__(self):
        return self.nombre

  
    

        # Modelo para representar los miembros del equipo en un proyecto.
class MiembroEquipo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=50)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.usuario.username} - {self.rol} en {self.proyecto.nombre}"