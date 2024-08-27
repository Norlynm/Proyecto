from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Perfil
#Este es el formulario personalizado
class FormularioPropio(forms.ModelForm):
    username = forms.CharField(label="Usuario",max_length=10,required=True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    email = forms.EmailField(required=True)
    first_name = forms.CharField( label='Nombre',max_length=30, required=True)
    last_name = forms.CharField( label='Apellido', max_length=30, required=True)

    class Meta:
        model = User
        fields =[ 'username', 'email', 'first_name', 'last_name', 'password1', 'password2']




class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['bio', 'Tareas_usuario','fecha_ingreso','user']
