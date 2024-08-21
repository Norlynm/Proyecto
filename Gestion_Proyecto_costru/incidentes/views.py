from django.shortcuts import render, redirect, get_object_or_404
from .models import Incidente
from .forms import IncidenteForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse


@login_required
def listar_incidentes(request):
    """
    Vista para listar todos los incidentes reportados.
    """
    incidentes = Incidente.objects.all()
    return render(request, 'incidentes/listar_incidentes.html', {'incidentes': incidentes})


@login_required  # Solo usuarios autenticados pueden reportar incidentes
def reportar_incidente(request):
    """
    Vista para reportar un nuevo incidente.
    Si la solicitud es POST, el formulario se valida y se guarda.
    Si es GET, se muestra el formulario vacío.
    """
    if request.method == 'POST':
        form = IncidenteForm(request.POST)
        if form.is_valid():
            incidente = form.save(commit=False)
            incidente.responsable = request.user  # Asignar el usuario que reporta el incidente
            incidente.save()
            return redirect('incidentes:listar_incidentes')
    else:
        form = IncidenteForm()
    
    return render(request, 'incidentes/reportar_incidente.html', {'form': form})

@login_required  # Permitir solo usuarios autenticados
def resolver_incidente(request, pk):
    """
    Vista para marcar un incidente como resuelto.
    """
    incidente = get_object_or_404(Incidente, pk=pk)
    if request.method == 'POST':
        incidente.estado = 'resuelto'
        incidente.save()
        return redirect('incidentes:listar_incidentes')
    return render(request, 'incidentes/resolver_incidente.html', {'incidente': incidente})




