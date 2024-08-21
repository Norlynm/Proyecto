from django import forms
from .models import Recurso

class RecursoForm(forms.ModelForm):
    class Meta:
        model = Recurso
        fields = ['nombre', 'tipo', 'cantidad', 'proyecto']
        labels = {
            'nombre': 'Nombre del Recurso',
            'tipo': 'Tipo de Recurso',
            'cantidad': 'Cantidad',
            'proyecto': 'Proyecto Asociado',
        }
