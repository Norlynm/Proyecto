from django import forms
from .models import Proyecto,Equipo,MiembroEquipo

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'equipo']  # Excluir 'estado'
        labels = {
            'nombre': 'Nombre del proyecto',
            'descripcion': 'Descripción del proyecto',
            'fecha_inicio': 'Fecha de inicio del proyecto',
            'fecha_fin': 'Fecha de finalización del proyecto',
            'equipo': 'Equipo'
        }

        widgets = {
         'fecha_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_fin': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    fecha_inicio = forms.DateTimeField(
        input_formats=['%d/%m/%Y %I:%M %p', '%Y-%m-%dT%H:%M'],  # Formatos permitidos
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    fecha_fin = forms.DateTimeField(
        input_formats=['%d/%m/%Y %I:%M %p', '%Y-%m-%dT%H:%M'],  # Formatos permitidos
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

class equiposForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre', 'descripcion', 'usuarios']
        widgets = {
            'usuarios': forms.CheckboxSelectMultiple,  # Para mostrar una lista de selección múltiple con checkboxes.
        }

    
        
class MiembroEquipoForm(forms.ModelForm):
    class Meta:
        model = MiembroEquipo
        fields =['usuario','rol','proyecto']