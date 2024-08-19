from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Notificacion
from django.urls import reverse

@login_required  # Asegura que solo los usuarios autenticados puedan acceder a las notificaciones
def listar_notificaciones(request):
    # Filtrar las notificaciones no leídas para el usuario actual
    notificaciones_no_leidas = Notificacion.objects.filter(usuario=request.user, leida=False)
    notificaciones_leidas = Notificacion.objects.filter(usuario=request.user, leida=True)

    # Renderiza la plantilla de las notificaciones y envía ambas listas de notificaciones
    return render(request, 'notifications/listar_notificaciones.html', {
        'notificaciones_no_leidas': notificaciones_no_leidas,
        'notificaciones_leidas': notificaciones_leidas,
    })

@login_required  # Solo los usuarios autenticados pueden marcar las notificaciones como leídas
def marcar_como_leida(request, pk):
    # Obtén la notificación correspondiente al id (pk)
    notificacion = get_object_or_404(Notificacion, pk=pk, usuario=request.user)
    
    # Marca la notificación como leída
    notificacion.leida = True
    notificacion.save()
    
    # Redirige a la página de lista de notificaciones
    return redirect(reverse('notifications:listar_notificaciones'))
