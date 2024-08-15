from django.views.generic import DetailView
from .models import Tarea
from django.urls import reverse_lazy
from django.shortcuts import render
from .forms import TareaForm
from django.views.generic import CreateView, ListView, UpdateView, DetailView


class CrearTarea(CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tareas/creartarea.html'
    success_url = reverse_lazy('tareas:listartareas')

class ListarTareas(ListView):
    model = Tarea
    template_name = 'tareas/tareas_detalle.html'
    context_object_name = 'tareas'

class ActualizarTarea(UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tareas/editartarea.html'
    success_url = reverse_lazy('tareas:listartareas')
    

class DetalleTarea(DetailView):
    model = Tarea
    template_name = 'tareas/tarea_detalle.html'
    context_object_name = 'tarea'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tarea = self.get_object()

        # Agregar lógica condicional
        if tarea.estado == 'pendiente':
            context['mensaje'] = "Esta tarea está pendiente."
        elif tarea.estado == 'completado':
            context['mensaje'] = "Esta tarea ya ha sido completada."
        
        return context
