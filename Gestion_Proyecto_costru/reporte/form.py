from django import forms
from .models import Reporte,Comentario

class ReporteForm(forms.ModelForm):
    class Meta:
        model = Reporte
        fields = ['archivo', 'descripcion', 'tipo', 'titulo','tareas','proyecto']  
        widgets = {
            'archivo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']