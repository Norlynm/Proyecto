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



from django.shortcuts import redirect
from django.views.generic import ListView
from .models import Tarea

class ListarTareas(ListView):
    model = Tarea
    template_name = 'tareas/listartareas.html'
    context_object_name = 'tareas'

    def post(self, request, *args, **kwargs):
        tarea_id = request.POST.get('tarea_id')
        nuevo_estado = request.POST.get('estado')
        tarea = Tarea.objects.get(id=tarea_id)
        tarea.estado = nuevo_estado  # Cambiar el estado
        tarea.save(update_fields=['estado'])  # Solo actualiza el campo estado
        return redirect('tareas:listartareas')

# buscador de tareas
from django.db.models import Q
from django.views.generic import ListView
from .models import Tarea

class ListarTareas(ListView):
    model = Tarea
    template_name = 'tareas/listartareas.html'
    context_object_name = 'tareas'

    def get_queryset(self):
        query = self.request.GET.get('q')  # Obtener el valor de búsqueda del formulario
        if query:
            # Filtrar por nombre de tarea, descripción y nombre de proyecto
            return Tarea.objects.filter(
                Q(nombre__icontains=query) |  # Buscar en el nombre de la tarea
                Q(descripcion__icontains=query) |  # Buscar en la descripción de la tarea
                Q(proyecto__nombre__icontains=query)  # Buscar en el nombre del proyecto relacionado
            )
        return Tarea.objects.all()  # Devolver todas las tareas si no hay búsqueda
    

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
