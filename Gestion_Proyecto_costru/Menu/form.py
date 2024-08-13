from django import forms
from django.contrib.auth.models import User

#Este es el formulario personalizado
class FormularioPropio(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    email = forms.EmailField(required=True)
    first_name = forms.CharField( label='Nombre',max_length=30, required=True)
    last_name = forms.CharField( label='Apellido', max_length=30, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user