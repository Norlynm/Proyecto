from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, AnonymousUser
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from .form import FormularioPropio
from proyectos.forms import ProyectoForm
from .models import Perfil
from.form import PerfilForm


def principal(request):
    return render(request, 'principal.html')

def registro(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {'form':FormularioPropio()})
    else:
        # Aqui se compara las contraseñas
        if request.POST['password1'] == request.POST['password2']:
            try:
              # Aqui se crea la clase usuario
                user = User.objects.create_user(
                    username=request.POST['username'], 
                    password=request.POST['password1'],
                    email=request.POST["email"],
                    first_name=request.POST["first_name"],
                    last_name=request.POST["last_name"],
                    
                    )
                user.save()
                login(request,user)
                #Aqui lo redirigira a otra pagina de la funcion tareas
                return redirect('Menu:principal')
            # Aqui estan las condiciones por si el usuario existe y por si no
    
            except IntegrityError:
                return render(request, 'registro.html', {
                    'form': FormularioPropio,
                    'error': 'El usuario ya existe'
                })
        
        return render(request, 'registro.html',{
                'form': FormularioPropio,
                'error': 'Contraseñas no coinciden'
            })


      
             

#Esta funcion cierra el usuario
def cerrar_sesion(request):
    logout(request)
    return redirect ('Menu:principal')
#Aqui se inicia sesion usando un formulario de Authentification 
def inicio_sesion(request):
    if request.method == 'GET':
        return render(request,'inicio_sesion.html', { 'form':AuthenticationForm})
       
         #Esta son condiciones para saber si el usuario o contraseñas son correctos        
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
            return redirect('Menu:principal')    
                 
     

from django.shortcuts import redirect

def usuario(request):
    if request.method == "POST" and 'cambiar' in request.POST:
        # Mostrar formulario editable
        usuario_form = FormularioPropio(instance=request.user)
        return render(request, 'usuario.html', {
            'form': usuario_form,
            'cambiar': True
        })

    elif request.method == "POST" and 'guardar' in request.POST:
        # Guardar cambios
        usuario_form = FormularioPropio(request.POST, instance=request.user)
        if usuario_form.is_valid():
            usuario_form.save()  # Guarda los cambios en el usuario
            return render(request, 'usuario.html', {
                'form': usuario_form,
                'mensaje': 'Los datos han sido actualizados correctamente',
                'cambiar': False  # Volver a la vista sin edición
            })
        else:
            return render(request, 'usuario.html', {
                'form': usuario_form,
                'error': 'Hubo un error con el formulario',
                'cambiar': True
            })

    elif request.method == "POST" and 'cancelar' in request.POST:
        # Redirigir a la página principal al cancelar
        return redirect('usuario.html')

    else:  # Método GET, solo mostrar los datos sin permitir edición
        usuario_form = FormularioPropio(instance=request.user)
        for field in usuario_form.fields.values():
            field.widget.attrs['readonly'] = True  # Hacer que todos los campos sean de solo lectura
        return render(request, 'usuario.html', {
            'form': usuario_form,
            'cambiar': False
        })

