from urllib import request
from django import forms
from django.urls import reverse_lazy
from .models import Proyecto
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProyectoForm,equiposForm
from .models import Proyecto,Equipo
from django.views.generic import CreateView,ListView, UpdateView, DeleteView,DetailView
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy


def inicio(request):
    return render(request, "proyectos/proyectos.html" )

class crearproyecto(CreateView,UserPassesTestMixin):
     model  = Proyecto
     form_class = ProyectoForm
     template_name = "proyectos/crearproyecto.html"
     success_url = reverse_lazy('proyectos:mostrarproyecto')
      # Esta función define la lógica para verificar si el usuario tiene acceso a la vista
def test_func(self):
        # Solo permitir al superusuario o administrador acceder a esta vista
        return self.request.user.is_superuser
   
class ListarProyecto(ListView,UserPassesTestMixin):
     model  = Proyecto
     template_name = "proyectos/proyecto_detalle.html"
     context_object_name = "proyecto"
     success_url = reverse_lazy('proyectos:listarproyecto')

class actulizarproyecto(UpdateView,UserPassesTestMixin):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'proyectos/editar_proyecto.html'
    success_url = reverse_lazy('proyectos:mostrarproyecto')
    context_object_name = "proyecto"
    
class eliminarproyecto(DeleteView,UserPassesTestMixin):
    model = Proyecto
    template_name = 'proyectos/eliminar_proyecto.html'
    success_url = reverse_lazy('proyectos:mostrarproyecto')
    context_object_name = 'proyecto'   
    


class crearequipo(CreateView,UserPassesTestMixin):
    model= Equipo
    form_class=equiposForm
    template_name= 'proyectos/equipos.html'
    success_url= reverse_lazy('proyectos:inicio')


class eliminarequipo(DeleteView, UserPassesTestMixin):
    model = Equipo
    template_name = 'proyectos/eliminarequipos.html'
    success_url = reverse_lazy('proyectos:inicio')
    context_object_name = 'equipo'

    # Método para verificar si el usuario tiene permiso
    def test_func(self):
        # Solo permitir al administrador o al superusuario eliminar equipos
        return self.request.user.is_superuser


class ListarEquipos(ListView):
    model = Equipo
    template_name = 'proyectos/mostrarequipo.html'
    context_object_name = 'equipos'

class editarequipo(UpdateView, UserPassesTestMixin):
    model = Equipo
    form_class = equiposForm
    template_name = 'proyectos/editar_equipo.html'
    success_url = reverse_lazy('proyectos:mostrarequipo')




#Autentificacion de los proyectos

def es_admin(user):
    return user.is_superuser

@user_passes_test(es_admin)
def asignar_proyectos(request):
    # Lógica para asignar proyectos
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proyectos:mostrarproyecto')
    else:
        form = ProyectoForm()

    return render(request, 'proyectos/crearproyecto.html', {'form': form})

from django.shortcuts import render
from Menu.models import Perfil
from proyectos.models import Proyecto
from tareas.models import Tarea

def perfil_usuario(request):
    perfil = Perfil.objects.get(user=request.user)
    proyectos = Proyecto.objects.filter(equipo=request.user)
    tareas = Tarea.objects.filter(asignado_a=request.user)

    return render(request, 'usuario/perfil.html', {
        'perfil': perfil,
        'proyectos': proyectos,
        'tareas': tareas,
    })
