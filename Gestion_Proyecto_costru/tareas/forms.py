from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['nombre', 'descripcion', 'proyecto', 'asignado_a', 'fecha_inicio', 'fecha_fin', 'prioridad']  
        labels = {
            'nombre': 'Nombre de la tarea',
            'descripcion': 'Descripción de la tarea',
            'proyecto': 'Proyecto asociado',
            'asignado_a': 'Asignado a',
            'fecha_inicio': 'Fecha de inicio',
            'fecha_fin': 'Fecha de finalización',
            'prioridad': 'Prioridad',
        }
    widgets = {
           'fecha_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_fin': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    # Aceptar varios formatos de fecha y hora
    fecha_inicio = forms.DateTimeField(
        input_formats=['%d/%m/%Y %I:%M %p', '%Y-%m-%dT%H:%M'],  # Formatos permitidos
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    fecha_fin = forms.DateTimeField(
        input_formats=['%d/%m/%Y %I:%M %p', '%Y-%m-%dT%H:%M'],  # Formatos permitidos
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )