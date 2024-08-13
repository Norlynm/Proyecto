from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, AnonymousUser
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError


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
                login(request,user)
                #Aqui lo redirigira a otra pagina de la funcion tareas
                return redirect(tareas)
            # Aqui estan las condiciones por si el usuario existe y por si no
    
            except IntegrityError:
                return render(request, 'registro.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        
        return render(request, 'registro.html',{
                'form': UserCreationForm,
                'error': 'Contraseñas no coinciden'
            })

#Funcion que lo que hace es que te lleva a la pagina de tareas
def tareas(request):
    return render(request, 'tareas.html')

#Esta funcion cierra el usuario
def cerrar_sesion(request):
    logout(request)
    return redirect (principal)
#Aqui se inicia sesion usando un formulario de Authentification 
def inicio_sesion(request):
    if request.method == 'GET':
        return render(request,'inicio_sesion.html', { 'form':AuthenticationForm})
       
         #Esta son condiciones para saber si el usuario o contraseñas son correcots        
    else:
        user = authenticate(username=request.POST['username'], password=request.POST['password']) 
        print(request.POST) 

        if user is None:
              return render(request,'inicio_sesion.html',{
            'form':AuthenticationForm,
            'error': 'Usuario o contraseña incorrectos'
      
        })       
        else:
            login(request, user)
            return redirect(principal)    
                 
     

def usuario(request):
    return render (request,'usuario.html')