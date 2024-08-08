from django.shortcuts import render
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
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return HttpResponse('Usuario creado con éxito')
            #Aqui estan las condiciones por si el usuario existe y por si no
            
            except:
                return HttpResponse('El usuario ya existe')
        else:
            return HttpResponse("Las contraseñas no coinciden")

 