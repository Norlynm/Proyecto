from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse


def principal(request):
    return render(request, 'principal.html')


def registro(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {'form': UserCreationForm()})
    else:
        # Aqui se compara las contraseñas
        if request.POST['password1'] == request.POST['password2']:
            try:
              # Aqui se crea la clase usuario
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return redirect(tareas)
            # Aqui estan las condiciones por si el usuario existe y por si no

            except:
                return render(request, 'registro.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        
        return render(request, 'registro.html',{
                'form': UserCreationForm,
                'error': 'Contraseñas no coinciden'
            })


def tareas(request):
    return render(request, 'tareas.html')
