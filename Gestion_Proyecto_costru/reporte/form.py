from django import forms
from .models import Reporte, Comentario

class ReporteForm(forms.ModelForm):
    class Meta:
        model = Reporte
        fields = ['archivo', 'descripcion', 'titulo', 'tareas', 'proyecto']
        widgets = {
            'archivo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'tareas': forms.SelectMultiple(attrs={'class': 'form-select'}),  # Select multiple para tareas
            'proyecto': forms.Select(attrs={'class': 'form-select'}),  # Select normal para proyectos
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto', 'reporte', 'usuario']
        widgets = {
            'texto': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'reporte': forms.Select(attrs={'class': 'form-select'}),
            'usuario': forms.Select(attrs={'class': 'form-select'}),
        }
