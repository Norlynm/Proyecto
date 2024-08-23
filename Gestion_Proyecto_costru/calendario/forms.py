from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'fecha', 'descripcion', 'proyecto']  
        labels = {
            'titulo': 'Título del Evento',
            'fecha': 'Fecha del Evento',
            'descripcion': 'Descripción',
            'proyecto': 'Proyecto asociado'
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'descripcion': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        }
