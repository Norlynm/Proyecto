from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento
from .forms import EventoForm  # Asegúrate de crear un formulario para manejar los eventos
from django.contrib.auth.decorators import login_required

@login_required  # Solo los usuarios autenticados pueden ver los eventos
def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'calendar/listar_eventos.html', {'eventos': eventos})

@login_required  # Solo los usuarios autenticados pueden agregar eventos
def agregar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.usuario = request.user  # Asociar el evento al usuario que lo crea
            evento.save()
            return redirect('calendar:listar_eventos')
    else:
        form = EventoForm()
    
    return render(request, 'calendar/agregar_evento.html', {'form': form})
