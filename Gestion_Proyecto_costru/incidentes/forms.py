from django import forms
from .models import Incidente

class IncidenteForm(forms.ModelForm):
    class Meta:
        model = Incidente
        fields = ['proyecto', 'descripcion', 'estado',]
        labels = {
            'proyecto': 'Proyecto Asociado',
            'descripcion': 'Descripción del Incidente',
            'estado': 'Estado del Incidente',
            'fecha': 'Fecha del Incidente',
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4, 'class': 'form-control', 'placeholder': 'Describe brevemente el incidente'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'proyecto': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
