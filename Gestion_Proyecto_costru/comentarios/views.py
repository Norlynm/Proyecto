from django.shortcuts import render, redirect, get_object_or_404
from .models import Comentario
from .forms import ComentarioForm  # Asegúrate de crear un formulario para manejar los comentarios
from django.contrib.auth.decorators import login_required
from tareas.models import Tarea  # Asegúrate de importar el modelo Tarea

@login_required  # Asegura que solo los usuarios autenticados puedan ver los comentarios
def listar_comentarios(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    comentarios = Comentario.objects.filter(tarea=tarea)
    return render(request, 'comments/listar_comentarios.html', {
        'tarea': tarea,
        'comentarios': comentarios
    })

@login_required  # Solo los usuarios autenticados pueden agregar comentarios
def agregar_comentario(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.tarea = tarea
            comentario.save()
            return redirect('comments:listar_comentarios', tarea_id=tarea.id)
    else:
        form = ComentarioForm()
    
    return render(request, 'comments/agregar_comentario.html', {
        'form': form,
        'tarea': tarea
    })
