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
from django.shortcuts import render
from proyectos.models import Proyecto  # Asegúrate de importar tu modelo de Proyecto
from tareas.models import Tarea  # Asegúrate de importar tu modelo de Tarea

def usuario(request):
    usuario_actual = request.user  # Obtener el usuario actual

    # Obtener proyectos en los que participa el usuario (relación con el equipo)
    proyectos_asignados = Proyecto.objects.filter(equipo__usuarios=usuario_actual)

    # Obtener tareas asignadas al usuario
    tareas_asignadas = Tarea.objects.filter(asignado_a=usuario_actual)

    # Si el método es POST, maneja el formulario de edición
    if request.method == "POST" and 'cambiar' in request.POST:
        usuario_form = FormularioPropio(instance=request.user)
        return render(request, 'usuario.html', {
            'form': usuario_form,
            'cambiar': True,
            'proyectos_asignados': proyectos_asignados,
            'tareas_asignadas': tareas_asignadas,
        })

    elif request.method == "POST" and 'guardar' in request.POST:
        usuario_form = FormularioPropio(request.POST, instance=request.user)
        if usuario_form.is_valid():
            usuario_form.save()
            return render(request, 'usuario.html', {
                'form': usuario_form,
                'mensaje': 'Los datos han sido actualizados correctamente',
                'cambiar': False,
                'proyectos_asignados': proyectos_asignados,
                'tareas_asignadas': tareas_asignadas,
            })
        else:
            return render(request, 'usuario.html', {
                'form': usuario_form,
                'error': 'Hubo un error con el formulario',
                'cambiar': True,
                'proyectos_asignados': proyectos_asignados,
                'tareas_asignadas': tareas_asignadas,
            })

    elif request.method == "POST" and 'cancelar' in request.POST:
        return redirect('usuario.html')

    else:
        usuario_form = FormularioPropio(instance=request.user)
        for field in usuario_form.fields.values():
            field.widget.attrs['readonly'] = True  # Campos de solo lectura
        return render(request, 'usuario.html', {
            'form': usuario_form,
            'cambiar': False,
            'proyectos_asignados': proyectos_asignados,
            'tareas_asignadas': tareas_asignadas,
        })

