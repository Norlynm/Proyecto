from django.shortcuts import render, redirect
from .models import Recurso
from .forms import RecursoForm
from django.contrib.auth.decorators import login_required

@login_required  # Solo los usuarios autenticados pueden ver y asignar recursos
def listar_recursos(request):
    """
    Vista para listar todos los recursos asignados a los proyectos.
    """
    recursos = Recurso.objects.all()
    return render(request, 'recursos/listar_recursos.html', {'recursos': recursos})

@login_required  # Solo los usuarios autenticados pueden asignar recursos
def asignar_recurso(request):
    """
    Vista para asignar nuevos recursos a los proyectos.
    Si la solicitud es POST, el formulario se valida y se guarda.
    Si es GET, se muestra el formulario vacío.
    """
    if request.method == 'POST':
        form = RecursoForm(request.POST)
        if form.is_valid():
            recurso = form.save(commit=False)
            recurso.save()
            return redirect('recursos:listar_recursos')
    else:
        form = RecursoForm()
    
    return render(request, 'recursos/asignar_recurso.html', {'form': form})
