from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['comentario']  # Solo incluimos el campo del comentario
        labels = {
            'comentario': 'Escribe tu comentario'
        }
        widgets = {
            'comentario': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        }
