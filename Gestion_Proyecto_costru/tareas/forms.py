from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['nombre', 'descripcion', 'proyecto', 'asignado_a', 'fecha_inicio', 'fecha_fin', 'prioridad']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'proyecto': forms.Select(attrs={'class': 'form-select'}),
            'asignado_a': forms.Select(attrs={'class': 'form-select'}),
            'fecha_inicio': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'fecha_fin': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'prioridad': forms.Select(attrs={'class': 'form-select'}),
        }

    # Aceptar varios formatos de fecha y hora para 'fecha_inicio' y 'fecha_fin'
    fecha_inicio = forms.DateTimeField(
        input_formats=['%d/%m/%Y %I:%M %p', '%Y-%m-%dT%H:%M'],  # Formatos permitidos
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'})
    )
    fecha_fin = forms.DateTimeField(
        input_formats=['%d/%m/%Y %I:%M %p', '%Y-%m-%dT%H:%M'],  # Formatos permitidos
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'})
    )
