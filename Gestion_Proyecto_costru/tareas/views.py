from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Tarea
from .forms import TareaForm
from django.views.generic import CreateView, ListView, UpdateView, DetailView

class CrearTarea(CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tareas/creartarea.html'
    success_url = reverse_lazy('tareas:listartareas')
    success_url = reverse_lazy('proyectos:inicio') 

class ListarTareas(ListView):
    model = Tarea
    template_name = 'tareas/tareas_detalle.html'
    context_object_name = 'tareas'

class ActualizarTarea(UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tareas/editartarea.html'
    success_url = reverse_lazy('tasks:listartareas')

class DetalleTarea(DetailView):
    model = Tarea
    template_name = 'tareas/tarea_detalle.html'
    context_object_name = 'tarea'
