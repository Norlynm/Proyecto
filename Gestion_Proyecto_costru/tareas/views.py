from django.views.generic import DetailView
from .models import Tarea
from django.urls import reverse_lazy
from django.shortcuts import render
from .forms import TareaForm
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView


def tarea(request):
    return render(request,'tareas/tareas.html')

class eliminarTarea(DeleteView):
    model = Tarea
    template_name = 'tareas/eliminartareas.html'
    success_url = reverse_lazy('tareas:listartareas')  # Redirige a la lista de tareas después de eliminar
    context_object_name = 'tarea'

class CrearTarea(CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tareas/creartarea.html'
    success_url = reverse_lazy('tareas:listartareas')

class ListarTareas(ListView):
    model = Tarea
    template_name = 'tareas/listartareas.html'
    context_object_name = 'tareas'

class ActualizarTarea(UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tareas/editartarea.html'
    success_url = reverse_lazy('tareas:listartareas')
    context_object_name = 'tarea'


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