from django import forms
from .models import Archivo

class ArchivoForm(forms.ModelForm):
    class Meta:
        model = Archivo
        fields = ['nombre', 'archivo', 'proyecto']  # Incluye los campos que quieras que el usuario pueda rellenar
        labels = {
            'nombre': 'Nombre del archivo',
            'archivo': 'Subir archivo',
            'proyecto': 'Proyecto asociado'
        }
