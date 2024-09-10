from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['nombre', 'descripcion', 'proyecto', 'asignado_a', 'fecha_inicio', 'fecha_fin', 'prioridad', 'estado']
        labels = {
            'nombre': 'Nombre de la tarea',
            'descripcion': 'Descripción de la tarea',
            'proyecto': 'Proyecto asociado',
            'asignado_a': 'Asignado a',
            'fecha_inicio': 'Fecha de inicio',
            'fecha_fin': 'Fecha de finalización',
            'prioridad': 'Prioridad',
            'estado': 'Estado'
        }
        widgets = {
             'fecha_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_fin': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
