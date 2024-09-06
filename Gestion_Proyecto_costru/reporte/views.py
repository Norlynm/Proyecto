from django.shortcuts import render
from .models import Reporte,Comentario
from.form import ReporteForm,ComentarioForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404, redirect

def crear_reporte(request):
    if request.method == 'POST':
        form = ReporteForm(request.POST, request.FILES)
        if form.is_valid():
            form= form.save(commit=False)
            reporte.usuario=request.user
            reporte.save()  
            form.save_m2m()
            return redirect('reporte:listar_reportes')
    else:
        form = ReporteForm()
    return render(request, 'reporte/crear_reportes.html', {'form': form})
    

def detalle_reporte(request, pk):
    reporte = get_object_or_404(Reporte, pk=pk)
    comentarios = reporte.comentarios.all()

    if request.method == "POST":
        comentario_form = ComentarioForm(request.POST)
        if comentario_form.is_valid():
            comentario = comentario_form.save(commit=False)
            comentario.reporte = reporte
            comentario.usuario = request.user
            comentario.save()
            return redirect('reporte:detalle_reporte', pk=pk)
    else:
        comentario_form = ComentarioForm()

    return render(request, 'reporte/detalle_reporte.html', {
        'reporte': reporte,
        'comentarios': comentarios,
        'comentario_form': comentario_form,
    })


def listar_reportes(request):
        reportes = Reporte.objects.all()  # Obtener todos los reportes
        return render(request, 'reporte/listar_reportes.html', {'reportes': reportes})
    