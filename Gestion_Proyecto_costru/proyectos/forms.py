from django import forms
from .models import Proyecto, Equipo, MiembroEquipo

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'equipo']
        labels = {
            'nombre': 'Nombre del proyecto',
            'descripcion': 'Descripción del proyecto',
            'fecha_inicio': 'Fecha de inicio del proyecto',
            'fecha_fin': 'Fecha de finalización del proyecto',
            'equipo': 'Equipo'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del proyecto'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción del proyecto'}),
            'fecha_inicio': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'fecha_fin': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'equipo': forms.Select(attrs={'class': 'form-select'}),
        }

        fecha_inicio = forms.DateTimeField(
        input_formats=['%d/%m/%Y %I:%M %p', '%Y-%m-%dT%H:%M'],  # Formatos permitidos
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'})  # Se añade la clase 'form-control'
    )
    
        fecha_fin = forms.DateTimeField(
        input_formats=['%d/%m/%Y %I:%M %p', '%Y-%m-%dT%H:%M'],  # Formatos permitidos
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'})  # Se añade la clase 'form-control'
    )
    
from django import forms
from .models import Equipo, MiembroEquipo

class equiposForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre', 'descripcion', 'usuarios']
        labels = {
            'nombre': 'Nombre del Equipo',
            'descripcion': 'Descripción del Equipo',
            'usuarios': 'Usuarios del Equipo',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del equipo'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese una descripción'}),
            'usuarios': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        }


class MiembroEquipoForm(forms.ModelForm):
    class Meta:
        model = MiembroEquipo
        fields = ['usuario', 'rol', 'proyecto']
        labels = {
            'usuario': 'Usuario',
            'rol': 'Rol',
            'proyecto': 'Proyecto',
        }
        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-select'}),
            'rol': forms.Select(attrs={'class': 'form-select'}),
            'proyecto': forms.Select(attrs={'class': 'form-select'}),
        }
