from urllib import request
from django import forms
from django.urls import reverse_lazy
from .models import Proyecto
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProyectoForm 
from .models import Proyecto
from django.views.generic import CreateView,ListView, UpdateView, DeleteView

def inicio(request):
    return render(request, "proyectos/inicio.html", )

class crearproyecto(CreateView):
     model  = Proyecto
     form_class = ProyectoForm
     template_name = "projects/crearproyecto.html"
     success_url = reverse_lazy('projects:mostrarproyecto')
     
   
class ListarProyecto(ListView):
     model  = Proyecto
     template_name = "proyectos/proyecto_detalle.html"
     context_object_name = "proyecto"

class actulizarproyecto(UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'proyectos/editar_proyecto.html'
    success_url = reverse_lazy('projects:mostrarproyecto')
    context_object_name = "proyecto"
    
class eliminarproyecto(DeleteView):
    model = Proyecto
    template_name = 'proyectos/eliminar_proyecto.html'
    success_url = reverse_lazy('projects:mostrarproyecto')
    context_object_name = 'proyecto'   